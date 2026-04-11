import os
import tarfile
import csv
from pathlib import Path
import soundfile as sf
import librosa
import io
from tqdm import tqdm
import sys

csv.field_size_limit(sys.maxsize)

root = "fleurs/data"
segmented_root = "fleurs_ipa/"
out_root = "processed_data"

def create_corpus_dir():
    N = len(os.listdir(root))
    for i, lang_dir in enumerate(os.listdir(root)):
        print(f"processing {lang_dir} ({i+1}/{N})")
        lang_path = os.path.join(root, lang_dir)
        if not os.path.isdir(lang_path):
            continue

        tsv_path = os.path.join(lang_path, "train.tsv")
        segmented_path = os.path.join(segmented_root, lang_dir, "train_sentences_input.txt")
        if not os.path.isfile(segmented_path):
            continue
        tar_path = os.path.join(lang_path, "audio", "train.tar.gz")
        if not (os.path.exists(tsv_path) and os.path.exists(tar_path)):
            continue

        out_dir = os.path.join(out_root, lang_dir, "textgrid_corpus_directory")
        if os.path.isdir(out_dir):
            continue
        Path(out_dir).mkdir(parents=True, exist_ok=True)

        entries = {}

        # Load TSV entries: filename → (sentence, speaker_id)
        with open(tsv_path, "r", encoding="utf-8") as f:
            with open(segmented_path, "r", encoding="utf-8") as f1:
                reader = csv.reader(f, delimiter="\t")
                reader1 = f1.read().splitlines()

                for row, txt in zip(reader, reader1):
                    wav_name = row[1]
                    try:
                        speaker_id = row[-2]
                    except:
                        print(row)
                    entries[wav_name] = (txt, speaker_id)

        # Extract wavs and create TextGrids
        with tarfile.open(tar_path, "r:gz") as tar:
            for member in tqdm(tar.getmembers()):
                name = os.path.basename(member.name)
                if name in entries:
                    sentence, speaker_id = entries[name]

                    speaker_dir = os.path.join(out_dir, speaker_id)
                    Path(speaker_dir).mkdir(parents=True, exist_ok=True)

                    wav_out = os.path.join(speaker_dir, name)

                    with tar.extractfile(member) as src:
                        data = src.read()
                        audio, sr = sf.read(io.BytesIO(data))

                        trimmed, _ = librosa.effects.trim(audio,top_db=15)

                        sf.write(wav_out, trimmed, sr)

                    txt_path = wav_out.replace(".wav", ".txt")

                    with open(txt_path, "w", encoding="utf-8") as f:
                        f.write(sentence.strip() + "\n") 

if __name__=='__main__':
    create_corpus_dir()