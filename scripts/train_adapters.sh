#!/bin/bash

set -e

if [ "$#" -lt 2 ]; then
    echo "Usage:"
    echo "  $0 <model_dir> <dataset>"
    echo
    echo "Examples:"
    echo "  $0 models/mms-300m-ipa fleurs"
    echo "  $0 models/mms-300m-ipa-doreco doreco_dataset"
    exit 1
fi

MODEL_DIR="$1"
DATASET="$2"

LEARNING_RATE="1e-4"
MAX_STEPS=500
WARMUP_RATIO=0.01

if [ "$DATASET" = "fleurs" ]; then

    LANGS=("af_za" "am_et" "ar_eg" "ast_es" "az_az" "be_by" "bg_bg" "bn_in" "ca_es" "ceb_ph" "ckb_iq" "cmn_hans_cn" "cs_cz" "cy_gb" "da_dk" "de_de" "el_gr" "en_us" "es_419" "et_ee" "fa_ir" "ff_sn" "fi_fi" "fr_fr" "ga_ie" "gl_es" "ha_ng" "he_il" "hi_in" "hr_hr" "hu_hu" "hy_am" "id_id" "it_it" "ja_jp" "jv_id" "ka_ge" "kk_kz" "km_kh" "kn_in" "ko_kr" "ky_kg" "lg_ug" "lo_la" "lt_lt" "lv_lv" "mi_nz" "mk_mk" "ml_in" "mn_mn" "mr_in" "ms_my" "mt_mt" "my_mm" "nb_no" "ne_np" "nl_nl" "ny_mw" "om_et" "or_in" "pa_in" "pl_pl" "ps_af" "pt_br" "ro_ro" "ru_ru" "sl_si" "sn_zw" "so_so" "sv_se" "sw_ke" "ta_in" "te_in" "tg_tj" "th_th" "tr_tr" "uk_ua" "ur_pk" "uz_uz" "vi_vn" "wo_sn" "xh_za" "yo_ng" "yue_hant_hk" "zu_za")

elif [ "$DATASET" = "doreco_dataset" ]; then

    mapfile -t LANGS < <(
        find doreco_dataset \
            -mindepth 1 \
            -maxdepth 1 \
            -type d \
            ! -name '.*' \
            -printf "%f\n" | sort
    )
    echo "Found ${#LANGS[@]} DoReCo languages"

else
    echo "Unknown dataset: $DATASET"
    exit 1
fi

for LANG in "${LANGS[@]}"; do

    echo "======================================"
    echo "Dataset : ${DATASET}"
    echo "Language: ${LANG}"
    echo "======================================"

    torchrun \
        --nproc_per_node=2 \
        train.py \
        --dataset "${DATASET}" \
        --model-dir "${MODEL_DIR}" \
        --target-lang "${LANG}" \
        --learning-rate "${LEARNING_RATE}" \
        --max-steps "${MAX_STEPS}" \
        --warmup-ratio "${WARMUP_RATIO}"

    echo "Finished training ${LANG}"
done
