# Forced Alignment Evaluation with Self-Supervised Speech Representations

## Overview
This repository contains notebooks, scripts, and experiment outputs for reproducing "Phoneme- and Word-Level Metrics Using Self-Supervised Speech Representations for Forced Alignment Evaluation".

## Repository layout
- Top-level notebooks: training, alignment, evaluation, and analysis notebooks such as train.ipynb, align.ipynb, eval.ipynb, and eval_mfa.ipynb.
- scripts/: preprocessing, training, and evaluation scripts including eval_aligns.py, eval_dataset.py, and the shell wrappers.
- results/: experiment artifacts, tuning summaries, evaluation JSON files, and plots generated during analysis.
- Required data folders: buckeye/, doreco/, fleurs/, fleurs_ipa/ for the different corpora used in the study.

## Requirements
- Tested with python 3.12
- Pip requirements are in requirements.txt

## Description of Tasks

### Processing FLEURS
- fleurs/ should contain sub-directory data/, which should be downloaded from [https://huggingface.co/datasets/google/fleurs](https://huggingface.co/datasets/google/fleurs)
- Then paste the data-loading script scripts/fleurs.py into fleurs/ for proper loading and incorporation of IPA transcripts.
- The notebook mfa.ipynb should be followed to produce fleurs_ipa_asr/ and fleurs_ipa/
- G2P requires a few dictionaries and G2P models for Chinese, Cantonese, and Hebrew. These should be downloaded (see [https://github.com/dmort27/epitran](https://github.com/dmort27/epitran)) and placed under epitran_dicts/ with the following structure:
  - epitran_dicts/cccanto-170202/: Cantonese dictionary files, including cccanto-webdist.txt.
  - epitran_dicts/cedict_1_0_ts_utf-8_mdbg/: Chinese dictionary files, including cedict_ts.u8.
  - epitran_dicts/phonikud-1.0.int8.onnx: ONNX model for Hebrew phoneme conversion used by Phonikud, that can be downloaded from [https://github.com/phonikud/phonikud](https://github.com/phonikud/phonikud)
- Many languages are not supported by the current num2words module. We have our own fixes, which are available in num2words_addons/. These should be incorporated into locally downloaded num2words from [https://github.com/savoirfairelinux/num2words](https://github.com/savoirfairelinux/num2words).

### Processing DoReCo
- doreco/ should contain sub-directory downloads/, where audio and annotation zip files for each language should be downloaded from [https://doreco.huma-num.fr/](https://doreco.huma-num.fr/)
- Each language should have a folder <glottocode>/ containing extracted audio file directory and a folder doreco_<glottocode>_core_v2/ containing extracted annotation directory
- Pre-processing should be done by following scripts/process_doreco.ipynb (paste it to doreco/), which produces directory doreco_dataset, that can be loaded by load_dataset.

### Processing Buckeye
- Download Buckeye corpus [https://buckeyecorpus.osu.edu/](https://buckeyecorpus.osu.edu/) to buckeye/. Resulting directory structure should be like buckeye/s01, buckeye/s02 ...
- Processed Buckeye corpus with perturbed alignments should be produced in buckeye_clean/ by following the latter part of mfa.ipynb.

### Running MFA on FLEURS
- mfa.yaml defines the MFA training configuration, including acoustic model settings, feature extraction, and the sequence of training stages (monophone, triphone, LDA, SAT).
- scripts/mfa.sh is the shell script used to train an MFA model per language and then generate alignments for the development/test corpus. Its requirements are:
  - MFA must be installed and available on the PATH as the mfa command. Follow the instructions at [https://montreal-forced-aligner.readthedocs.io/en/latest/getting_started.html](https://montreal-forced-aligner.readthedocs.io/en/latest/getting_started.html)
  - The preprocessing step in scripts/pre_process.py must have already produced the expected corpus directories under fleurs_ipa/.
  - If no model archive exists at processed_data_train/<lang>/<lang>_model.zip, the script will run MFA training; otherwise it will reuse the existing model.
  - Alignment outputs on test set are written to alignments/mfa/<lang> and are skipped if that directory already exists.

### Training Phoneme Models on FLEURS and DoReCo
- Models should be first initialized following the section "Configure" in train.ipynb
- Training should be done by executing the script scripts/train.sh, which also calls script to train adapters

### Phoneme Recognition Predictions
- Outputs from phoneme recognition models (ASR) for further analysis can be saved by following eval.ipynb

### Alignment using Phoneme Models
- Simply run the following to generate alignments for all the models on FLEURS and DoReCo in alignments/
    > `python scripts/ctc_align.py`
- For running on phonologically complex Archi and Rutul, follow align.ipynb taking datasets and phoneme models from [https://github.com/mahesh-ak/north_caucasian_asr](https://github.com/mahesh-ak/north_caucasian_asr)

### Evaluation of Alignments
- The metrics PCMI and WACS are defined in scripts/eval_aligns.py
- Complete evaluation of the alignments generated in the previous step can be done by executing:
    > `python scripts/eval_dataset.py`

### Perturbation experiments
- Perturbation and hyperparameter tuning experiments are present in eval_mfa.ipynb

### Plotting and Tabulating Results
- The plots and tables are generated by following Analysis.ipynb


