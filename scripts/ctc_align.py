from typing import List, Optional
import ctc_segmentation
import numpy as np
from transformers import Wav2Vec2Tokenizer, Wav2Vec2Processor, Wav2Vec2ForCTC
from lingpy.sequence.sound_classes import ipa2tokens
from praatio import textgrid
from datasets import load_dataset, concatenate_datasets, DownloadConfig
import os
import logging
from itertools import islice
from tqdm.auto import tqdm
import torch
import soundfile as sf

SILENCE_RATIO=0.05
MIN_WORD_DUR=0.04
MIN_PHONE_DUR=0.02

def save_test_audio(audio, path):
    sf.write(
        path,
        audio["array"],
        audio["sampling_rate"]
    )

def get_doreco_langs():
    return sorted(
        d
        for d in os.listdir("doreco_dataset")
        if os.path.isdir(os.path.join("doreco_dataset", d))
        and not d.startswith(".")
    )

def batch_iterator(iterable, batch_size):
    iterator = iter(iterable)

    while True:
        batch = list(islice(iterator, batch_size))

        if not batch:
            break

        yield batch

logging.basicConfig(level=logging.ERROR)

download_config = DownloadConfig(
    local_files_only=True,
    cache_dir=".cache",   # optional
)

LANGS = ['af_za', 'am_et', 'ar_eg', 'ast_es', 'az_az', 'be_by', 'bg_bg', 'bn_in', 'ca_es', 'ceb_ph', 'ckb_iq', 'cmn_hans_cn', 'cs_cz', 'cy_gb', 'da_dk', 'de_de', 'el_gr', 'en_us', 'es_419', 'et_ee', 'fa_ir', 'ff_sn', 'fi_fi', 'fr_fr', 'ga_ie', 'gl_es', 'ha_ng', 'he_il', 'hi_in', 'hr_hr', 'hu_hu', 'hy_am', 'id_id', 'it_it', 'ja_jp', 'jv_id', 'ka_ge', 'kk_kz', 'km_kh', 'kn_in', 'ko_kr', 'ky_kg', 'lg_ug', 'lo_la', 'lt_lt', 'lv_lv', 'mi_nz', 'mk_mk', 'ml_in', 'mn_mn', 'mr_in', 'ms_my', 'mt_mt', 'my_mm', 'nb_no', 'ne_np', 'nl_nl', 'ny_mw', 'om_et', 'or_in', 'pa_in', 'pl_pl', 'ps_af', 'pt_br', 'ro_ro', 'ru_ru', 'sl_si', 'sn_zw', 'so_so', 'sv_se', 'sw_ke', 'ta_in', 'te_in', 'tg_tj', 'th_th', 'tr_tr', 'uk_ua', 'ur_pk', 'uz_uz', 'vi_vn', 'wo_sn', 'xh_za', 'yo_ng', 'yue_hant_hk', 'zu_za']


def _build_intervals_with_pauses(
    segments,
    xmin,
    xmax,
    min_gap=0.0005,
):
    """
    Fill gaps between segments with silence intervals,
    while enforcing:
      - monotonic intervals
      - no overlaps
      - minimum duration/gap

    segments: list of dicts with keys:
        [start, end, text]
    """

    intervals = []

    # sort for safety
    segments = sorted(segments, key=lambda x: x["start"])

    cur = float(xmin)

    for seg in segments:

        start = round(float(seg["start"]), 4)
        end = round(float(seg["end"]), 4)
        text = seg["text"]

        # ---------------------------------
        # prevent backward movement
        # ---------------------------------
        if start < cur:
            start = cur

        # ---------------------------------
        # enforce minimum duration
        # ---------------------------------
        if end <= start:
            end = start + min_gap

        # ---------------------------------
        # insert silence gap if needed
        # ---------------------------------
        if start - cur >= min_gap:
            intervals.append((cur, start,""))

        # ---------------------------------
        # add segment
        # ---------------------------------
        intervals.append((start, end, text))

        # next interval must begin AFTER this
        cur = end

    # ---------------------------------
    # tail silence
    # ---------------------------------
    if xmax - cur >= min_gap:
        intervals.append((cur,float(xmax),""))

    return intervals


def save_textgrids(
    audio_filenames,
    alignments,
    out_dir,
    audio_durs,
):
    """
    Args:
        audio_paths: List[str]
        alignments: List[dict] with keys "words", "phones"
        out_dir: output directory
    """

    os.makedirs(out_dir, exist_ok=True)

    for filename, align, audio_dur in zip(audio_filenames, alignments, audio_durs):
        words = align["words"]
        phones = align["phones"]

        xmax = audio_dur

        xmin = 0.0

        # build tiers (with pauses filled)
        word_intervals = _build_intervals_with_pauses(words, xmin, xmax)
        phone_intervals = _build_intervals_with_pauses(phones, xmin, xmax)

        # create TextGrid
        tg = textgrid.Textgrid()

        word_tier = textgrid.IntervalTier(
            name="words",
            entries=word_intervals,
            minT=xmin,
            maxT=xmax,
        )

        phone_tier = textgrid.IntervalTier(
            name="phones",
            entries=phone_intervals,
            minT=xmin,
            maxT=xmax,
        )

        tg.addTier(word_tier)
        tg.addTier(phone_tier)

        # output filename
        name = os.path.splitext(filename)[0] + ".TextGrid"
        out_path = os.path.join(out_dir, name)

        # save
        tg.save(out_path, format="short_textgrid", includeBlankSpaces=True)

def phones_to_string(example):
    """
    Convert
    words:
        je
        suis
    phones:
        ʒ ə s ɥ i
    into
        ʒə sɥi

    (spaces only at word boundaries)
    """

    phones = example["phones"]
    words = example["words"]

    if len(phones) == 0:
        return "", ""

    pieces = []
    word_pieces = []

    phone_idx = 0

    for word in words:
        wstart = word["start"]
        wend = word["end"]
        current = []
        while phone_idx < len(phones):
            ph = phones[phone_idx]
            center = 0.5 * (
                ph["start"] + ph["end"]
            )
            if center >= wend:
                break
            if center >= wstart:
                current.append(ph["phone"])
            phone_idx += 1

        if current:
            pieces.append("".join(current))
            word_pieces.append(word["text"])

    return " ".join(pieces), " ".join(word_pieces)

def build_gold_alignment(ex):
    phones = ex["phones"]
    words = ex["words"]
    gold_phones = [
        {
            "text": ph["phone"],
            "start": float(ph["start"]),
            "end": float(ph["end"]),
        }
        for ph in phones
    ]
    gold_words = [
        {
            "text": w["text"],
            "start": float(w["start"]),
            "end": float(w["end"])
        }
        for w in words
    ] 

    return {
        "words": gold_words,
        "phones": gold_phones,
    }

def make_doreco_filename(lang, idx):
    return f"{lang}_{idx:08d}.wav"
    
class CTCSegmentation:
    
    def __init__(self, tokenizer: Wav2Vec2Tokenizer= None, sampling_rate: int= 16000):
        self.tokenizer = tokenizer
        if tokenizer:
            char_list = [tokenizer.convert_ids_to_tokens(i) for i in range(tokenizer.vocab_size)]
            self.config = ctc_segmentation.CtcSegmentationParameters(char_list=char_list)
            self.sampling_rate = sampling_rate
        else:
            char_list = ['<unk>']
            self.config = ctc_segmentation.CtcSegmentationParameters(char_list=char_list)
            self.sampling_rate = 16_000
        self.total_failures = 0
        

    def get_word_and_timestamps_batch(
        self,
        probs_batch: List[np.ndarray],
        audio_lens: List[int],
        frame_lens: List[int],
        ipa_transcripts: Optional[List[str]],
        transcripts: Optional[List[str]],
    ) -> List[dict]:

        alignments = []
        
        
        # --- Transcript handling ---
        if not ipa_transcripts:
            pred_ids = probs_batch.argmax(axis=-1)
            ipa_transcripts = self.tokenizer.batch_decode(pred_ids)

        if not transcripts:
            transcripts = ipa_transcripts
            
        for probs, audio_len, frame_len, ipa_transcript, transcript in zip(probs_batch, audio_lens, frame_lens, ipa_transcripts, transcripts):
            
            
            self.config.index_duration = ( audio_len / self.sampling_rate ) / frame_len
            # =====================
            # WORD ALIGNMENT
            # =====================
            words_ipa = ipa_transcript.split()
            words = transcript.split()

            assert len(words) == len(words_ipa)
            

            try:
                gt_mat, utt_idx = ctc_segmentation.prepare_text(self.config, words_ipa)
                probs = probs[:frame_len]
                timings, char_probs, _ = ctc_segmentation.ctc_segmentation(
                    self.config, probs, gt_mat
                )
    
                word_segments = ctc_segmentation.determine_utterance_segments(
                    self.config, utt_idx, char_probs, timings, words_ipa
                )


            except:
                # tokenize all words into phones
                self.total_failures += 1
                all_word_phones = []
            
                for w_ipa in words_ipa:
                    if w_ipa != "<unk>":
                        phs = ipa2tokens(w_ipa, merge_vowels=False)
                    else:
                        phs = ["<unk>"]
            
                    all_word_phones.append(phs)
            
                phone_counts = [len(phs) for phs in all_word_phones]
                total_phones = sum(phone_counts)
            
                total_duration = frame_len * self.config.index_duration
            
                current = 0.0
                word_segments = []
            
                for n_ph in phone_counts:
                    dur = total_duration * (n_ph / total_phones)
            
                    word_segments.append(
                        (current, current + dur, 0.0)
                    )
            
                    current += dur


            word_out = [
                {
                    "text": w,
                    "start": float(p[0]),
                    "end": float(p[1]),
                    "conf": float(p[2]),
                }
                for w, p in zip(words, word_segments)
            ]

            # =====================
            # PHONE ALIGNMENT (hierarchical)
            # =====================
            
            phone_out = []
            
            PAD_FRAMES = 0
            
            for word, word_ipa, seg in zip(words, words_ipa, word_out):
            
                # ---------------------------------
                # convert word timestamps -> frames
                # ---------------------------------
                start_frame = int(seg["start"] / self.config.index_duration)
            
                end_frame = int(seg["end"] / self.config.index_duration)
            
                # add small context padding
                start_frame = max(0, start_frame - PAD_FRAMES)
                if probs is not None:
                    end_frame = min(len(probs), end_frame + PAD_FRAMES)
                else:
                    end_frame = end_frame
            
            
                # ---------------------------------
                # tokenize IPA word
                # ---------------------------------
                if word_ipa != '<unk>':
                    phones = ipa2tokens(word_ipa, merge_vowels=False)
                else:
                    phones = ['<unk>']
                
            
                
                try:
                    # crop local probabilities
                    local_probs = probs[start_frame:end_frame]
                    gt_mat_p, utt_idx_p = ctc_segmentation.prepare_text(self.config, phones)
                    timings_p, char_probs_p, _ = (
                        ctc_segmentation.ctc_segmentation(
                            self.config,
                            local_probs,
                            gt_mat_p
                        )
                    )
                
            
                    phone_segments = (
                        ctc_segmentation.determine_utterance_segments(
                            self.config,
                            utt_idx_p,
                            char_probs_p,
                            timings_p,
                            phones
                        )
                    )
                    
                except:
                    unit = max(0.001, (end_frame - start_frame)*self.config.index_duration/len(phones))
                    phone_segments = [(i*unit, (i+1)*unit, 0.0) for i, ph in enumerate(phones)]
            
                # ---------------------------------
                # convert local -> global timestamps
                # ---------------------------------
                word_phone_out = []
            
                for ph, p in zip(phones, phone_segments):
            
                    global_start = (p[0]+ start_frame * self.config.index_duration)
            
                    global_end = (p[1]+ start_frame * self.config.index_duration)
            
                    global_start = float(global_start)
                    global_end = float(global_end)

            
                    word_phone_out.append(
                        {
                            "text": ph,
                            "start": global_start,
                            "end": global_end,
                            "conf": round(float(p[2]), 3),
                        }
                    )
            
                phone_out.extend(word_phone_out)
                

            alignments.append({
                "words": word_out,
                "phones": phone_out,
            })
        return alignments


def detect_speech_bounds(audio, factor=0.05):
    energy = np.abs(audio)

    # smooth over ~25ms
    smooth = np.convolve(
        energy,
        np.ones(400) / 400,
        mode="same"
    )

    threshold = factor * np.percentile(smooth, 95)

    idx = np.where(smooth > threshold)[0]

    if len(idx) == 0:
        return 0, len(audio)

    return idx[0], idx[-1]

def compute_global_threshold(
    audio,
    factor=SILENCE_RATIO,
):

    energy=np.abs(audio)

    smooth=np.convolve(
        energy,
        np.ones(400)/400,
        mode="same"
    )

    thr=factor*np.percentile(
        smooth,
        95
    )

    return smooth,thr

def trim_interval(
    smooth,
    sr,
    thr,
    start,
    end,
):

    s=int(start*sr)
    e=int(end*sr)

    if e<=s:
        return start,end

    chunk=smooth[s:e]

    idx=np.where(
        chunk>thr
    )[0]

    if len(idx)==0:
        return start,end

    ns=(s+idx[0])/sr
    ne=(s+idx[-1])/sr

    if ne-ns<MIN_WORD_DUR:
        return start,end

    return float(ns),float(ne)

def trim_alignment_silence(
    alignment,
    audio,
    sr=16000,
    silence_ratio=SILENCE_RATIO,
    min_word_dur=MIN_WORD_DUR,
    min_phone_dur=MIN_PHONE_DUR,
):
    """
    alignment:
        {
            "words": [...],
            "phones": [...]
        }

    audio:
        np.ndarray
    """

    smooth, thr = compute_global_threshold(
        audio,
        factor=silence_ratio,
    )

    words = alignment["words"]
    phones = alignment["phones"]

    # -----------------------------
    # trim words
    # -----------------------------

    for w in words:

        ns, ne = trim_interval(
            smooth,
            sr,
            thr,
            w["start"],
            w["end"],
        )

        w["start"] = float(ns)
        w["end"] = float(ne)

    # -----------------------------
    # propagate trims to phones
    # -----------------------------

    if len(phones) > 0:

        for w in words:

            contained = []

            for ph in phones:

                if ph["text"].strip() == "":
                    continue

                overlap = (
                    ph["end"] > w["start"]
                    and ph["start"] < w["end"]
                )

                if overlap:
                    contained.append(ph)

            if not contained:
                continue

            first = contained[0]
            last = contained[-1]

            if first["start"] < w["start"]:

                new_start = min(
                    w["start"],
                    first["end"] - min_phone_dur,
                )

                if new_start < first["end"]:
                    first["start"] = float(new_start)

            if last["end"] > w["end"]:

                new_end = max(
                    w["end"],
                    last["start"] + min_phone_dur,
                )

                if new_end > last["start"]:
                    last["end"] = float(new_end)

        alignment["phones"] = [
            ph
            for ph in phones
            if ph["end"] > ph["start"]
        ]

    return alignment

def alignData(dataset="fleurs", align_dir="alignments", model_path=None, device=None, save_audio=False, trim_silence=False, split='test'):
    if not device:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if os.path.exists(model_path):
        processor = Wav2Vec2Processor.from_pretrained(model_path)
        model = Wav2Vec2ForCTC.from_pretrained(model_path)
        tokenizer = processor.tokenizer
    else:
        processor = None
        model = None
        tokenizer = None
    
    if model:
        model.eval()
        model.to(device)
    
    output_path = os.path.join(align_dir, os.path.basename(model_path) if model_path[-1] != '/' else os.path.basename(model_path[:-1]))
    if trim_silence:
        output_path += "-SIL"
    os.makedirs(output_path, exist_ok=True)

    if processor:
        ctc_segmentor = CTCSegmentation(tokenizer=processor.tokenizer)
    else:
        ctc_segmentor = CTCSegmentation()
    
    if dataset == "fleurs":
        langs = LANGS
    else:
        langs = get_doreco_langs()
    for lang in tqdm(langs):

        if dataset == "fleurs":
            lang_dataset = load_dataset(
                "fleurs",
                lang,
                streaming=True,
                download_config=download_config,
                trust_remote_code=True,
            )
        else:
            lang_dataset = load_dataset(
                "doreco_dataset",
                data_dir=lang,
                streaming=True,
            )

        if split != 'all':
            test_dataset = lang_dataset[split]   # streaming dataset
        else:
            # lazily chain all available splits into one streaming dataset
            splits = [
                lang_dataset[s]
                for s in ['train', 'test', 'validation']
                if s in lang_dataset
            ]
            test_dataset = splits[0] if len(splits) == 1 else concatenate_datasets(splits)

        if model:
            model.load_adapter(lang)
        alignments = []
        audio_filenames = []
        audio_durs = []

        gold_alignments = []

        for batch in batch_iterator(test_dataset, batch_size=2):

            # audio arrays
            audios = [x["audio"]["array"][:360000] for x in batch]
            if dataset == "fleurs":
                ipa_transcripts = [x["ipa"] for x in batch]
                transcripts = [x["word_segmented"] for x in batch]
            else:
                ipa_transcripts = []
                transcripts = []
                for x in batch:
                    phs, wrds = phones_to_string(x)
                    ipa_transcripts.append(phs)
                    transcripts.append(wrds)
            if model:
                # processor handles padding dynamically
                inputs = processor(
                    audios,
                    sampling_rate=16000,
                    return_tensors="pt",
                    padding=True,
                )
    
                inputs = {k: v.to(device) for k, v in inputs.items()}
                audio_lengths = inputs["attention_mask"].sum(-1)
                logit_lengths = model._get_feat_extract_output_lengths(audio_lengths).cpu().numpy()
                audio_lengths = audio_lengths.cpu().numpy()
                with torch.no_grad():
                    logits = model(**inputs).logits
    
                probs_batch = torch.softmax(logits, dim=-1).cpu().numpy()
            
            else:
                audio_lengths = []
                probs_batch = []
                logit_lengths = []
                speech_offsets = []
        
                for audio in audios:
                    start, end = detect_speech_bounds(audio)
                    speech_offsets.append((start, end))
                    audio_lengths.append(end - start)
                    probs_batch.append(None)
                    logit_lengths.append(100)

            alignments_batch = ctc_segmentor.get_word_and_timestamps_batch(
                    probs_batch=probs_batch,
                    audio_lens=audio_lengths,
                    frame_lens=logit_lengths,
                    ipa_transcripts=ipa_transcripts,
                    transcripts=transcripts
                )
            if trim_silence:
                alignments_batch = [
                    trim_alignment_silence(
                        alignment,
                        audio,
                        sr=16000,
                    )
                    for alignment, audio in zip(
                        alignments_batch,
                        audios,
                    )
                ]
            if not model:
                for alignment, (start_sample, _) in zip(alignments_batch, speech_offsets):
    
                    offset_sec = start_sample / 16000
            
                    for item in alignment["words"]:
                        item["start"] = item["start"] + offset_sec
                        item["end"] = item["end"] + offset_sec
            
                    for item in alignment["phones"]:
                        item["start"] = item["start"] + offset_sec
                        item["end"] = item["end"] + offset_sec

            alignments.extend(alignments_batch)
            audio_durs.extend([ (audio.shape[0] if hasattr(audio, "shape") else len(audio)) / 16000 for audio in audios])
            if dataset == "fleurs":
                audio_filenames.extend(
                    [
                        os.path.basename(x["audio"]["path"])
                        for x in batch
                    ]
                )
            else:
                start_idx = len(audio_filenames)
                for i, ex in enumerate(batch):
                    fname = make_doreco_filename(
                        lang,
                        start_idx + i
                    )
                    audio_filenames.append(fname)
                    if save_audio:
                        wav_dir = os.path.join(
                            output_path,
                            lang,
                            "audio"
                        )
                        os.makedirs(wav_dir, exist_ok=True)
                        save_test_audio(
                            ex["audio"],
                            os.path.join(wav_dir, fname)
                        )
                        gold_alignments.append(
                            build_gold_alignment(ex)
                        )
        save_textgrids(
            audio_filenames,
            alignments,
            os.path.join(output_path, lang),
            audio_durs
        )
        if save_audio:
            save_textgrids(
                audio_filenames,
                gold_alignments,
                os.path.join(output_path, lang, "gold"),
                audio_durs,
            )
        
    print("Total failures:", ctc_segmentor.total_failures)
    
    
if __name__=="__main__":
    fleurs_models = ['random', 'models/mms-300m-ipa', 'models/w2v2-lv-60-espeak-ipa']
    doreco_models = ['random_doreco', 'models/mms-300m-ipa-doreco']

    for model in fleurs_models:
        alignData(dataset='fleurs', align_dir="alignments", model_path=model, trim_silence=False)
        if 'random' not in model:
            alignData(dataset='fleurs', align_dir="alignments", model_path=model, trim_silence=True)
    
    for model in doreco_models:
        alignData(dataset='doreco_dataset', align_dir="alignments", model_path=model, trim_silence=False)
        if 'random' not in model:
            alignData(dataset='doreco_dataset', align_dir="alignments", model_path=model, trim_silence=True)
        else:
            alignData(dataset='doreco_dataset', align_dir="alignments", model_path=model, trim_silence=False, save_audio=True)
   

   