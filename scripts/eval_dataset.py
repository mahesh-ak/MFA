import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "2"
os.environ["OMP_NUM_THREADS"] = "2"

from datasets import load_dataset, DownloadConfig
from itertools import islice

download_config = DownloadConfig(
    local_files_only=True,
    cache_dir=".cache",   # optional
)

def batch_iterator(iterable, batch_size):
    iterator = iter(iterable)

    while True:
        batch = list(islice(iterator, batch_size))

        if not batch:
            break

        yield batch

LANGS = ['af_za', 'am_et', 'ar_eg', 'ast_es', 'az_az', 'be_by', 'bg_bg', 'bn_in', 'ca_es', 'ceb_ph', 'ckb_iq', 'cmn_hans_cn', 'cs_cz', 'cy_gb', 'da_dk', 'de_de', 'el_gr', 'en_us', 'es_419', 'et_ee', 'fa_ir', 'ff_sn', 'fi_fi', 'fr_fr', 'ga_ie', 'gl_es', 'ha_ng', 'he_il', 'hi_in', 'hr_hr', 'hu_hu', 'hy_am', 'id_id', 'it_it', 'ja_jp', 'jv_id', 'ka_ge', 'kk_kz', 'km_kh', 'kn_in', 'ko_kr', 'ky_kg', 'lg_ug', 'lo_la', 'lt_lt', 'lv_lv', 'mi_nz', 'mk_mk', 'ml_in', 'mn_mn', 'mr_in', 'ms_my', 'mt_mt', 'my_mm', 'nb_no', 'ne_np', 'nl_nl', 'ny_mw', 'om_et', 'or_in', 'pa_in', 'pl_pl', 'ps_af', 'pt_br', 'ro_ro', 'ru_ru', 'sl_si', 'sn_zw', 'so_so', 'sv_se', 'sw_ke', 'ta_in', 'te_in', 'tg_tj', 'th_th', 'tr_tr', 'uk_ua', 'ur_pk', 'uz_uz', 'vi_vn', 'wo_sn', 'xh_za', 'yo_ng', 'yue_hant_hk', 'zu_za']

from eval_aligns import ForcedAlignEval, ForcedAlignEvalConfig
from scipy.io import wavfile
from tqdm import tqdm
import numpy as np
import os, json, gc
# ---------------------------------------------------------
# AAS
# ---------------------------------------------------------
from difflib import SequenceMatcher
import numpy as np
import textgrid

def load_tg(path,word_tier="words",phone_tier="phones"):
    tg=textgrid.TextGrid.fromFile(path)

    def tier2list(name):
        tier=[t for t in tg.tiers if t.name==name][0]
        out=[]
        for x in tier:
            out.append({
                "start":float(x.minTime),
                "end":float(x.maxTime),
                "text":x.mark
            })
        return out

    return tg.maxTime,tier2list(word_tier),tier2list(phone_tier)
    
def compute_aas(gold,pred):

    def align_and_score(g,p):

        gl=[x["text"] for x in g]
        pl=[x["text"] for x in p]

        sm=SequenceMatcher(a=gl,b=pl)

        errs=[]

        for tag,i1,i2,j1,j2 in sm.get_opcodes():

            if tag=="equal":

                for gx,px in zip(g[i1:i2],p[j1:j2]):

                    e=(
                        abs(gx["start"]-px["start"])+
                        abs(gx["end"]-px["end"])
                    )/2

                    errs.append(e)

            else:
                # insertion/deletion/substitution
                bad=g[i1:i2]

                for x in bad:
                    errs.append(x["end"]-x["start"])

        if len(errs)==0:
            return None, None
        
        return 1000*np.mean(errs), np.array(errs)

    _,gw,gp=load_tg(gold)
    _,pw,pp=load_tg(pred)

    waas, errs =align_and_score(gw,pw)
    paas, _ =align_and_score(gp,pp)

    return {
        "word_aas_ms":round(float(waas),3) if waas is not None else None,
        "phone_aas_ms":round(float(paas),3) if paas is not None else None,
    }
    
# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------
LANGS=LANGS
DORECO_LANGS = sorted(
        d
        for d in os.listdir("doreco_dataset")
        if os.path.isdir(os.path.join("doreco_dataset", d))
        and not d.startswith(".")
    )

ALIGN_DIRS=[
#    "alignments/qwen3-FA/",
#    "alignments/mms-300m-ipa/",
#    "alignments/random/",
#    "alignments/mfa/",
#    "alignments/w2v2-lv-60-espeak-ipa/",
    "alignments/gold_doreco",
    "alignments/random_doreco/",
    "alignments/mms-300m-ipa-doreco-SIL/",
    "alignments/mms-300m-ipa-doreco/",
#    "alignments/w2v2-lv-60-espeak-ipa-doreco-SIL/",
#    "alignments/w2v2-lv-60-espeak-ipa-doreco/",
]

MODELS=[
    "facebook/mms-300m",
    "facebook/wav2vec2-large-xlsr-53"
]

SAMPLE_SIZE=250


# ---------------------------------------------------------
# EVALUATORS
# ---------------------------------------------------------
evaluators={}

for model_name in MODELS:

    cfg=ForcedAlignEvalConfig(
        model=model_name,
    )

    evaluators[model_name]=ForcedAlignEval(cfg)

# ---------------------------------------------------------
# RESULTS STRUCTURE
# results[align_dir][lang][model]
# ---------------------------------------------------------
results={}

for align_dir in ALIGN_DIRS:

    results[align_dir]={}

# ---------------------------------------------------------
# MATERIALIZE ONE LANGUAGE
# ---------------------------------------------------------
def materialize_language(lang):

    ds=load_dataset(
        "fleurs",
        lang,
        split="test",
        streaming=True,
        download_config=download_config,
        trust_remote_code=True
    )

    ds=ds.shuffle(buffer_size=500).take(SAMPLE_SIZE)

    items=[]

    for x in ds:

        try:

            items.append({
                "audio":x["audio"]["array"][:360000].astype(np.float32),
                "wav_file":os.path.basename(x["audio"]["path"])
            })

        except Exception as e:

            print(lang,e)

    return items

def materialize_doreco_language(lang, root):

    audio_dir = os.path.join(root, lang, "audio")

    items = []

    for wav_file in sorted(os.listdir(audio_dir)):

        if not wav_file.endswith(".wav"):
            continue

        wav_path = os.path.join(audio_dir, wav_file)

        sr, audio = wavfile.read(wav_path)

        if audio.dtype != np.float32:
            audio = audio.astype(np.float32)

            if np.issubdtype(audio.dtype, np.integer):
                audio /= np.iinfo(audio.dtype).max

        items.append(
            {
                "audio": audio,
                "wav_file": wav_file,
            }
        )

    return items
    
# ---------------------------------------------------------
# RESOLVE TEXTGRIDS
# ---------------------------------------------------------
def resolve_tg_paths(items,align_dir,lang, gold=False):

    if not gold:
        tg_roots=[os.path.join(align_dir,lang)]
    else:
        tg_roots=[os.path.join(align_dir,lang,'gold')]

    if "mfa" in align_dir:

        tg_root=tg_roots[0]

        tg_roots=[
            os.path.join(tg_root,f)
            for f in os.listdir(tg_root)
            if os.path.exists(os.path.join(tg_root,f))
        ]

    resolved=[]

    for item in items:

        found=None

        for tg_root in tg_roots:

            tg_path=os.path.join(
                tg_root,
                os.path.splitext(item["wav_file"])[0]+".TextGrid"
            )

            if os.path.exists(tg_path):

                found=tg_path
                break

        resolved.append(found)

    return resolved

# ---------------------------------------------------------
# GENERATORS
# ---------------------------------------------------------
def audio_iter(items):

    for x in items:
        yield x["audio"]

def tg_iter(tg_paths):

    for tg in tg_paths:
        yield tg



for lang in tqdm(LANGS,desc="languages"):
    if not os.path.exists(os.path.join(align_dir, lang)):
        continue
    # -------------------------------------
    # materialize ONCE for this language
    # -------------------------------------
    items=materialize_language(lang)

    if len(items)==0:
        continue

    # -------------------------------------
    # evaluate all alignment dirs
    # and all embedding models
    # -------------------------------------
    for align_dir in ALIGN_DIRS:
        if 'doreco' in align_dir:
            continue

        results[align_dir][lang]={}

        tg_paths=resolve_tg_paths(
            items,
            align_dir,
            lang
        )

        for model_name,evaluator in evaluators.items():

            metrics=evaluator.compute_metrics(
                audios=audio_iter(items),
                tg_paths=tg_iter(tg_paths)
            )

            results[align_dir][lang][model_name]=metrics

            print(
                lang,
                os.path.basename(align_dir.rstrip("/")),
                model_name.split("/")[-1],
                metrics["nmi"]["nmi"] if metrics["nmi"] else None,
                metrics["wacs"]["wacs"] if metrics["wacs"] else None
            )


    # -------------------------------------
    # free memory before next language
    # -------------------------------------
    del items
    gc.collect()

for lang in tqdm(DORECO_LANGS, desc="languages"):

    items = materialize_doreco_language(
        lang,
        "alignments/random_doreco",
    )

    if len(items) == 0:
        continue

    # -------------------------------------
    # evaluate all alignment dirs
    # and all embedding models
    # -------------------------------------
    for align_dir in ALIGN_DIRS:
        if 'doreco' not in align_dir:
            continue

        results[align_dir][lang]={}

        if 'gold' not in align_dir:
            tg_paths=resolve_tg_paths(
                items,
                align_dir,
                lang
            )
        else:
            tg_paths = resolve_tg_paths(items, "alignments/random_doreco", lang, gold=True)

        for model_name,evaluator in evaluators.items():

            metrics=evaluator.compute_metrics(
                audios=audio_iter(items),
                tg_paths=tg_iter(tg_paths)
            )
            gold_tg_paths = resolve_tg_paths(items, "alignments/random_doreco", lang, gold=True)
            
            aas_scores = []
            
            for gold_tg, pred_tg in zip(gold_tg_paths, tg_paths):
                
                aas_scores.append(compute_aas(gold_tg, pred_tg))

            
            metrics["aas"] = {
                "word_aas_ms": float(
                    np.mean(
                        [
                            x["word_aas_ms"]
                            for x in aas_scores
                            if x["word_aas_ms"] is not None
                        ]
                    )
                ),
                "phone_aas_ms": float(
                    np.mean(
                        [
                            x["phone_aas_ms"]
                            for x in aas_scores
                            if x["phone_aas_ms"] is not None
                        ]
                    )
                ),
            }

            results[align_dir][lang][model_name]=metrics
            print(
                lang,
                os.path.basename(align_dir.rstrip("/")),
                model_name.split("/")[-1],
                metrics["nmi"]["nmi"] if metrics["nmi"] else None,
                metrics["wacs"]["wacs"] if metrics["wacs"] else None,
                metrics["aas"]
            )


    # -------------------------------------
    # free memory before next language
    # -------------------------------------
    del items
    gc.collect()


# -----------------------------------------------------
# SAVE PER ALIGNMENT DIRECTORY
# -----------------------------------------------------
for align_dir in ALIGN_DIRS:

    align_name=os.path.basename(
        align_dir.rstrip("/")
    )

    os.makedirs(os.path.join("results", align_name), exist_ok=True)
    out_path=os.path.join( "results",
        align_name,
        f"alignment_results.json"
    )

    with open(out_path,"w") as fp:

        json.dump(
            results[align_dir],
            fp,
            indent=2
        )

    print(f"saved -> {out_path}")