import argparse
from datasets import load_dataset, DownloadConfig
import torch
from transformers import (
    Wav2Vec2Processor,
    Wav2Vec2Config,
    Wav2Vec2ForCTC,
    TrainingArguments,
    Trainer,
)
import numpy as np
import evaluate
from dataclasses import dataclass
from typing import List, Dict
from pathlib import Path


LANGS = ['af_za', 'am_et', 'ar_eg', 'ast_es', 'az_az', 'be_by', 'bg_bg', 'bn_in', 'ca_es', 'ceb_ph', 'ckb_iq', 'cmn_hans_cn', 'cs_cz', 'cy_gb', 'da_dk', 'de_de', 'el_gr', 'en_us', 'es_419', 'et_ee', 'fa_ir', 'ff_sn', 'fi_fi', 'fr_fr', 'ga_ie', 'gl_es', 'ha_ng', 'he_il', 'hi_in', 'hr_hr', 'hu_hu', 'hy_am', 'id_id', 'it_it', 'ja_jp', 'jv_id', 'ka_ge', 'kk_kz', 'km_kh', 'kn_in', 'ko_kr', 'ky_kg', 'lg_ug', 'lo_la', 'lt_lt', 'lv_lv', 'mi_nz', 'mk_mk', 'ml_in', 'mn_mn', 'mr_in', 'ms_my', 'mt_mt', 'my_mm', 'nb_no', 'ne_np', 'nl_nl', 'ny_mw', 'om_et', 'or_in', 'pa_in', 'pl_pl', 'ps_af', 'pt_br', 'ro_ro', 'ru_ru', 'sl_si', 'sn_zw', 'so_so', 'sv_se', 'sw_ke', 'ta_in', 'te_in', 'tg_tj', 'th_th', 'tr_tr', 'uk_ua', 'ur_pk', 'uz_uz', 'vi_vn', 'wo_sn', 'xh_za', 'yo_ng', 'yue_hant_hk', 'zu_za']
def prepare_batch(batch, processor):
    audios = [x["array"][:360000] for x in batch["audio"]]
    sampling_rate = batch["audio"][0]["sampling_rate"]

    inputs = processor(
        audios,
        sampling_rate=sampling_rate,
        padding=False,   # IMPORTANT: no padding here
    )

    labels = processor.tokenizer(batch["labels_text"]).input_ids

    return {
        "input_values": inputs["input_values"],
        "attention_mask": inputs["attention_mask"],
        "labels": labels,
    }

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
        return ""

    pieces = []

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

    return " ".join(pieces)

@dataclass
class DataCollatorCTCWithPadding:
    processor: Wav2Vec2Processor

    def __call__(self, features: List[Dict]):
        # separate inputs and labels
        input_features = [
            {
                "input_values": f["input_values"],
                "attention_mask": f["attention_mask"],
            }
            for f in features
        ]

        label_features = [{"input_ids": f["labels"]} for f in features]

        # pad audio
        batch = self.processor.pad(
            input_features,
            padding=True,
            return_tensors="pt",
        )

        # pad labels
        labels_batch = self.processor.tokenizer.pad(
            label_features,
            padding=True,
            return_tensors="pt",
        )

        # mask padding
        labels = labels_batch["input_ids"].masked_fill(
            labels_batch["attention_mask"].ne(1), -100
        )

        batch["labels"] = labels
        return batch

    
wer_metric = evaluate.load("wer")
cer_metric = evaluate.load("cer")


def compute_metrics(pred, processor):
    pred_logits = pred.predictions
    pred_ids = np.argmax(pred_logits, axis=-1)

    # decode predictions
    pred_str = processor.batch_decode(pred_ids)

    # replace -100 in labels
    label_ids = pred.label_ids.copy()
    label_ids[label_ids == -100] = processor.tokenizer.pad_token_id

    # decode labels
    label_str = processor.batch_decode(label_ids, group_tokens=False)

    # compute metrics
    wer = wer_metric.compute(predictions=pred_str, references=label_str)
    cer = cer_metric.compute(predictions=pred_str, references=label_str)

    return {
        "wer": wer,
        "cer": cer,
    }
    
   
    
def parse_args():
    parser = argparse.ArgumentParser(
        description="Train a Wav2Vec2 model for ASR on a given dataset."
    )
    
    parser.add_argument(
        "--model-dir",
        type=str,
        required=True,
        help="Pretrained model path from local directory. Processor should also be present in the same directory. Checkpoints will be saved in this directory.",
    )

    parser.add_argument(
        "--dataset",
        type=str,
        default="fleurs",
        choices=["fleurs", "doreco_dataset"],
    )

    parser.add_argument(
        "--target-lang",
        type=str,
        default='all',
        help=f"Valid individual languages"
    )
    
    parser.add_argument(
        "--batch-size",
        type=int,
        default=2,
    )
    parser.add_argument(
        "--learning-rate",
        type=float,
        default=1e-5,
    )
    
    parser.add_argument(
        "--max-steps",
        type=int,
        default=20000,
    )
    
    parser.add_argument(
        "--warmup-ratio",
        type=float,
        default=0.01,
    )
    
    return parser.parse_args()

def main():

    args = parse_args()
    
    print('\n'.join(f'{k}: {v}' for k, v in vars(args).items()))

    ## load and prepare fleurs dataset

    download_config = DownloadConfig(
        local_files_only=True,
        cache_dir=".cache",   # optional
    )

    if args.dataset == "fleurs":
        dataset = load_dataset(
            "fleurs",
            args.target_lang,
            streaming=True,
            download_config=download_config,
            trust_remote_code=True,
        )
    elif args.dataset == "doreco_dataset":
        if args.target_lang == "all":
            dataset = load_dataset(
                "doreco_dataset",
                streaming=True,
                trust_remote_code=True,
            )
        else:
            dataset = load_dataset(
                "doreco_dataset",
                data_dir=args.target_lang,
                streaming=True,
                trust_remote_code=True,
            )
    
    processor = Wav2Vec2Processor.from_pretrained(args.model_dir)

    if args.dataset == "doreco_dataset":
        def add_labels(example):
            example["labels_text"] = phones_to_string(example)
            return example

        dataset = dataset.map(add_labels)

    else:

        def add_labels(example):
            example["labels_text"] = example["ipa"]
            return example

        dataset = dataset.map(add_labels)
        
    dataset = dataset.map(lambda x: prepare_batch(x, processor= processor), batched=True, batch_size=32, remove_columns=dataset['train'].column_names)

    data_collator = DataCollatorCTCWithPadding(processor=processor)
    
    ## prepare model and training
    
    if args.target_lang == 'all':
        model = Wav2Vec2ForCTC.from_pretrained(args.model_dir)
        model.freeze_feature_encoder()
    else:
        model = Wav2Vec2ForCTC.from_pretrained(args.model_dir, target_lang= args.target_lang)
        for name, param in model.named_parameters():
            param.requires_grad = ("adapter" in name) or ("lm_head" in name)

    
    training_args = TrainingArguments(
        output_dir=args.model_dir,
        # batch / optimization
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        gradient_accumulation_steps= (16 // 2) // args.batch_size,   # effective batch = 16, 2 devices
        learning_rate=args.learning_rate,
        
        # schedule
        warmup_ratio=args.warmup_ratio,
        lr_scheduler_type="cosine",
        max_steps=args.max_steps,   # REQUIRED for streaming
        
        # precision
        fp16=torch.cuda.is_available(),
        
        # logging / saving
        save_steps=args.max_steps // 10,
        save_total_limit=2,
        
        # evaluation (optional)
        eval_strategy="steps",
        eval_steps=args.max_steps // 10,
        eval_accumulation_steps = 32,
        
        # misc
        report_to="none",   # or "wandb"
        load_best_model_at_end=True,
        metric_for_best_model="wer",
        greater_is_better=False,
        remove_unused_columns=True,
        accelerator_config={"dispatch_batches": False},
    )
    
    train_dataset = dataset["train"]#.shuffle(buffer_size=8000, seed=42)
    eval_dataset = dataset["validation"].take(1000)#.shuffle(buffer_size=8000, seed=42)
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
        processing_class=processor,
        compute_metrics=lambda x: compute_metrics(x, processor),
    )
    
    trainer.train()

    processor.save_pretrained(args.model_dir)
    model.save_pretrained(args.model_dir)
   
    if args.target_lang != 'all': 
        adapter_state = {
            k: v.cpu()
            for k, v in model.state_dict().items()
            if ("adapter" in k) or ("lm_head" in k)
        }

        torch.save(
            adapter_state,
            f"{args.model_dir}/adapter.{args.target_lang}.bin"
        )

    else:
        ## Initialize adapters

        if args.dataset == "fleurs":
            # Assume LANGS already exists somewhere
            langs = LANGS
        elif args.dataset == "doreco_dataset":
            langs = sorted(
                p.name
                for p in Path("doreco_dataset").iterdir()
                if p.is_dir() and '.' not in p 
            )

        print(
            f"Initializing adapters for "
            f"{len(langs)} languages"
        )

        for lang in langs:
            config = Wav2Vec2Config.from_pretrained(args.model_dir)
            config.adapter_attn_dim = 16
            tmp_model = Wav2Vec2ForCTC.from_pretrained(
                args.model_dir,
                config=config,
                ignore_mismatched_sizes=True,
            )
            tmp_model.freeze_feature_encoder()

            adapter_state = {
                k: v.cpu()
                for k, v in tmp_model.state_dict().items()
                if ("adapter" in k) or ("lm_head" in k)
            }

            torch.save(
                adapter_state,
                f"{args.model_dir}/adapter.{lang}.bin"
            )

            del tmp_model

if __name__=='__main__':
    main()