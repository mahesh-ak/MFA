#!/usr/bin/env bash

python scripts/pre_process.py

set -e

ROOT="processed_data_train"
TEST_ROOT="processed_data_test"
LEX_ROOT="fleurs_ipa"
CONFIG="mfa.yaml"
NUM_JOBS=4

for lang_dir in "$ROOT"/*; do
    [ -d "$lang_dir" ] || continue

    lang=$(basename "$lang_dir")

    corpus_dir="$lang_dir/textgrid_corpus_directory"
    test_corpus_dir="$TEST_ROOT/$lang/textgrid_corpus_directory"
    lexicon="$LEX_ROOT/$lang/lexicon.txt"
    model="$lang_dir/${lang}_model.zip"
    align_out="alignments/mfa/$lang"

    echo "==== Processing $lang ===="

    if [ ! -f "$lexicon" ]; then
        echo "Skipping $lang (no lexicon)"
        continue
    fi

    if [ ! -f "$model" ]; then
        # -----------------------
        # Train
        # -----------------------
        echo "Training $lang..."
        if ! mfa train "$corpus_dir" "$lexicon" "$model" \
            --config_path "$CONFIG" \
            --num_jobs "$NUM_JOBS" \
            --single_speaker \
            --clean; then

            echo "❌ Training failed for $lang, skipping..."
            echo "$lang" >> failed_langs.txt
            continue
        fi
    fi

    if [ ! -d "$corpus_dir" ]; then
        echo "Skipping $lang (no corpus dir)"
        continue
    fi

    if [ -d "$align_out" ]; then
        echo "Skipping $align_out (alignments exist)"
        continue
    fi


    # -----------------------
    # Align
    # -----------------------
    echo "Aligning $lang..."
    if ! mfa align "$test_corpus_dir" "$lexicon" "$model" "$align_out" \
        --num_jobs "$NUM_JOBS" \
        --single_speaker \
        --retry_beam 100 \
        --clean; then

        echo "❌ Alignment failed for $lang, skipping..."
        echo "$lang" >> failed_langs.txt
        continue
    fi

    echo "Done $lang"
    echo
done