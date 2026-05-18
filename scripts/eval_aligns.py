import numpy as np
import torch
import parselmouth
from parselmouth.praat import call
from transformers import Wav2Vec2Model, Wav2Vec2FeatureExtractor
from collections import defaultdict
import os
from dataclasses import dataclass
from typing import Tuple, Iterator
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import normalized_mutual_info_score
from fastdtw import fastdtw
from scipy.spatial.distance import cosine
from collections import Counter
from scipy.stats import entropy



class W2V2Embedding:
    
    def __init__(self, model_str, layer_range = (12, 16)):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = Wav2Vec2FeatureExtractor.from_pretrained(model_str)
        self.model = Wav2Vec2Model.from_pretrained(model_str).to(self.device)
        self.sampling_rate = self.processor.sampling_rate
        self.layer_range = layer_range
        self.model.eval()
    
    @torch.no_grad()
    def extract_embeddings_batch(self, audios):
        results = []

        inputs = self.processor(
            audios,
            sampling_rate=self.sampling_rate,
            return_tensors="pt",
            padding=True
        )

        input_values = inputs.input_values.to(self.device)
        attention_mask = inputs.attention_mask.to(self.device)
        outputs = self.model(input_values, attention_mask=attention_mask, output_hidden_states=True)
        hidden = torch.stack(outputs.hidden_states[self.layer_range[0]:self.layer_range[1]]).mean(0)
        # sample lengths
        input_lengths = attention_mask.sum(-1).cpu().numpy()

        # exact wav2vec2 frame lengths
        frame_lengths = self.model._get_feat_extract_output_lengths(torch.tensor(input_lengths)).cpu().numpy()

        for i in range(len(audios)):
            
            num_samples = int(input_lengths[i])
            duration = num_samples / self.sampling_rate
            num_frames = int(frame_lengths[i])
            
            emb = hidden[i, :num_frames].cpu().numpy()
            
            # frame timestamps
            frame_times = np.linspace(0,duration,num_frames,endpoint=False)

            results.append((emb, frame_times))

        return results
    
    
# -----------------------------
# TEXTGRID PARSING
# -----------------------------
def load_textgrid(tg_path, tier_names=["phones", "words"]):
    tg = parselmouth.read(tg_path)
    out = {}
    n_tiers = call(tg, "Get number of tiers")

    for tier_name in tier_names:
        tier_exists = False
        for i in range(1, n_tiers + 1):
            name = call(tg, "Get tier name", i)
            if name == tier_name:
                tier_index = i
                tier_exists = True
                break

        if tier_exists:
            intervals = []
            n_intervals = call(tg, "Get number of intervals", tier_index)

            for j in range(1, n_intervals + 1):
                start = call(tg, "Get start time of interval", tier_index, j)
                end = call(tg, "Get end time of interval", tier_index, j)
                label = call(tg, "Get label of interval", tier_index, j)

                if label.strip() == "":
                    label = "sil"

                intervals.append((start, end, label))
            out[tier_name] = intervals

    return out


def assign_labels_to_frames(frame_times, intervals):
    labels = []
    j = 0
    for t in frame_times:
        while j < len(intervals) - 1 and t > intervals[j][1]:
            j += 1
        labels.append(intervals[j][2])
    return labels


def pool_emb(x, k=2):
    n=len(x)//k
    if n==0: return x
    return x[:n*k].reshape(n,k,-1).mean(1)

def crop_frames(emb, frame_times, start, end):
    idx=(frame_times>=start)&(frame_times<=end)
    return emb[idx]

def dtw_sim(x,y):
    if len(x)<2 or len(y)<2: return None
    x=x/np.maximum(np.linalg.norm(x,axis=1,keepdims=True),1e-8)
    y=y/np.maximum(np.linalg.norm(y,axis=1,keepdims=True),1e-8)
    x,y=pool_emb(x),pool_emb(y)
    distance, path =fastdtw(x,y,dist=cosine)
    return 1 - distance/len(path)

@dataclass
class ForcedAlignEvalConfig:
    
    model : str = "facebook/mms-300m"
    layer_range: Tuple[int, int] = (15, 16)
    batch_size : int = 2

    samples_phon_eval : int = 50
    max_frames : int = 10_000
    n_clusters : int = 50

    samples_word_eval : int = 200
    max_words: int = 200
    min_occ : int = 3
    max_pairs: int = 10
    

class ForcedAlignEval:
    
    def __init__(self, config=ForcedAlignEvalConfig()):
        self.config=config
        self.emb_model = W2V2Embedding(config.model, config.layer_range)
    
    def collect_embeddings(self,audios:Iterator[np.ndarray],tg_paths:Iterator[str])-> dict:

        all_frame_embs=[]
        all_frame_labels=[]
        word2embs=defaultdict(list)

        processed=0

        sample_size=max(
            self.config.samples_word_eval,
            self.config.samples_phon_eval
        )

        batch_size=self.config.batch_size

        while processed<sample_size:

            batch_audios=[]
            batch_tgs=[]

            for _ in range(min(batch_size,sample_size-processed)):

                try:
                    audio=next(audios)
                    tg_path=next(tg_paths)
                except StopIteration:
                    break

                batch_audios.append(audio[:360000])
                batch_tgs.append(tg_path)

            if len(batch_audios)==0:
                break

            batch_results=self.emb_model.extract_embeddings_batch(batch_audios)

            for (emb,frame_times),tg_path in zip(batch_results,batch_tgs):

                if tg_path is None or not os.path.exists(tg_path):
                    continue

                # -------------------------
                # phone/frame collection
                # -------------------------
                intervals=load_textgrid(tg_path)
                if processed < self.config.samples_phon_eval and "phones" in intervals:
                    labels=assign_labels_to_frames(
                        frame_times,
                        intervals["phones"]
                    )

                    all_frame_embs.append(emb)
                    all_frame_labels.extend(labels)

                # -------------------------
                # word collection
                # -------------------------

                if processed < self.config.samples_word_eval and "words" in intervals:
                    for start,end,label in intervals["words"]:

                        label=label.strip().lower()

                        if not label or label in ["sp","sil","<unk>"]:
                            continue

                        wemb=crop_frames(emb,frame_times,start,end)

                        if len(wemb)>=4:
                            word2embs[label].append(wemb)

            processed+=len(batch_audios)

        return {
            "frame_embeddings":all_frame_embs,
            "frame_labels":all_frame_labels,
            "word_embeddings":word2embs
        } 
        
        
    def compute_metrics(self, audios:Iterator[np.ndarray], tg_paths:Iterator[str])-> dict:

        # -------------------------
        # NMI
        # -------------------------
        data = self.collect_embeddings(audios=audios, tg_paths=tg_paths)
        all_embeddings=data["frame_embeddings"]
        all_labels=data["frame_labels"]

        nmi=None

        if len(all_embeddings):

            X=np.concatenate(all_embeddings,axis=0)
            y=np.array(all_labels)

            if len(X)>self.config.max_frames:

                label_to_indices=defaultdict(list)

                for i,label in enumerate(y):
                    label_to_indices[label].append(i)

                freqs={
                    label:len(indices)
                    for label,indices in label_to_indices.items()
                }

                weights={
                    label:np.sqrt(freq)
                    for label,freq in freqs.items()
                }

                total_weight=sum(weights.values())
                selected=[]

                for label,indices in label_to_indices.items():

                    n=int(self.config.max_frames*weights[label]/total_weight)
                    n=min(n,len(indices))

                    chosen=np.random.choice(indices, n, replace=False)

                    selected.extend(chosen)

                selected=np.array(selected)

                X=X[selected]
                y=y[selected]

            norms=np.linalg.norm(X,axis=1,keepdims=True)
            norms[norms==0]=1

            X=(X/norms).astype(np.float16)

            cluster_ids=MiniBatchKMeans(
                n_clusters=self.config.n_clusters,
                batch_size=1000
            ).fit_predict(X)

            nmi= {"nmi": float(normalized_mutual_info_score(y, cluster_ids))}
            cluster_sizes=np.bincount(cluster_ids,minlength=self.config.n_clusters)
            cluster_probs=cluster_sizes/cluster_sizes.sum()

            cluster_ent=float(entropy(cluster_probs))
            cluster_ent_norm=float(cluster_ent/np.log(len(cluster_probs)))

            label_counts=Counter(y)
            label_probs=np.array(list(label_counts.values()),dtype=np.float64)
            label_probs/=label_probs.sum()

            label_ent=float(entropy(label_probs))
            label_ent_norm=float(label_ent/np.log(len(label_probs)))

            cluster_purity=[]

            for k in range(self.config.n_clusters):

                idx=(cluster_ids==k)

                if idx.sum()==0:
                    continue

                labels_k=y[idx]
                counts=Counter(labels_k)

                purity=max(counts.values())/len(labels_k)
                cluster_purity.append(purity)

            nmi.update({
                "cluster_entropy":cluster_ent,
                "cluster_entropy_norm":cluster_ent_norm,
                "label_entropy":label_ent,
                "label_entropy_norm":label_ent_norm,
                "mean_cluster_purity":float(np.mean(cluster_purity)),
                "std_cluster_purity":float(np.std(cluster_purity)),
                "frames":int(len(X)),
                "labels":int(len(label_counts)),
                "clusters_used":int((cluster_sizes>0).sum())
            })
        # -------------------------
        # WACS
        # -------------------------
        word2embs=data["word_embeddings"]

        pos_sims=[]
        neg_sims=[]

        vocab=[
            w for w,v in word2embs.items()
            if len(v)>=self.config.min_occ
        ]


        vocab=sorted(
            vocab,
            key=lambda x:len(word2embs[x]),
            reverse=True
        )[:self.config.max_words]

        for word in vocab:

            embs=word2embs[word]
            pairs=0

            for i in range(len(embs)):
                for j in range(i+1,len(embs)):

                    sim=dtw_sim(embs[i],embs[j])

                    if sim is not None:
                        pos_sims.append(sim)

                    pairs+=1

                    if pairs>=self.config.max_pairs:
                        break

                if pairs>=self.config.max_pairs:
                    break

            neg_words=np.random.choice(
                vocab,
                min(5,len(vocab)),
                replace=False
            )

            for nw in neg_words:

                if nw==word:
                    continue

                x=embs[np.random.randint(len(embs))]
                y=word2embs[nw][
                    np.random.randint(len(word2embs[nw]))
                ]

                sim=dtw_sim(x,y)

                if sim is not None:
                    neg_sims.append(sim)

        wacs=None

        if len(pos_sims) and len(neg_sims):

            pos=float(np.mean(pos_sims))
            neg=float(np.mean(neg_sims))

            # ---- WACS enrichments ----
            pos_std=float(np.std(pos_sims))
            neg_std=float(np.std(neg_sims))

            # Cohen's d
            eps=1e-8
            pooled=np.sqrt(
                (
                    ((len(pos_sims)-1)*(pos_std**2))+
                    ((len(neg_sims)-1)*(neg_std**2))
                )/
                max(1,(len(pos_sims)+len(neg_sims)-2))
            )+eps

            cohen_d=(pos-neg)/pooled

            # overlap estimate
            wacs_margin=pos-neg
            snr=wacs_margin/(pos_std+neg_std+eps)

            wacs={
                "positive":pos,
                "negative":neg,
                "wacs":wacs_margin,
                "positive_std":pos_std,
                "negative_std":neg_std,
                "cohen_d":float(cohen_d),
                "snr":float(snr),
                "positive_pairs":int(len(pos_sims)),
                "negative_pairs":int(len(neg_sims)),
                "positive_min":float(np.min(pos_sims)),
                "positive_max":float(np.max(pos_sims)),
                "negative_min":float(np.min(neg_sims)),
                "negative_max":float(np.max(neg_sims)),
                "vocab_size": len(vocab)
            }
                        

        return {
            "nmi":nmi,
            "wacs":wacs
        }