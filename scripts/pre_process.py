import os
import tarfile
from pathlib import Path
from tqdm import tqdm

root = "fleurs/data"
segmented_root = "fleurs_ipa/"
split = "test"
out_root = f"processed_data_{split}"

def create_corpus_dir():
    N = len(os.listdir(root))
    for i, lang_dir in enumerate(os.listdir(root)):

        print(f"processing {lang_dir} ({i+1}/{N})")
        lang_path = os.path.join(root, lang_dir)
        if not os.path.isdir(lang_path):
            continue

        tsv_path = os.path.join(lang_path, f"{split}.tsv")
        segmented_path = os.path.join(segmented_root, lang_dir, f"{split}_sentences_input.txt")
        if not os.path.isfile(segmented_path):
            continue
        tar_path = os.path.join(lang_path, "audio", f"{split}.tar.gz")
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
                reader = f.read().splitlines()
                reader1 = f1.read().splitlines()

                for row, txt in zip(reader, reader1):
                    row = row.split('\t')
                    wav_name = row[1]
                    speaker_id = row[-1]

                    entries[wav_name] = (txt, speaker_id)

        # Extract wavs and create TextGrids
        with tarfile.open(tar_path, "r:gz") as tar:
            for member in tqdm(tar.getmembers()):
                name = os.path.basename(member.name)
                if name in entries:
                    try:
                        sentence, speaker_id = entries[name]

                        speaker_dir = os.path.join(out_dir, speaker_id)
                        Path(speaker_dir).mkdir(parents=True, exist_ok=True)

                        wav_out = os.path.join(speaker_dir, name)

                        with tar.extractfile(member) as src, open(wav_out, "wb") as dst:
                            dst.write(src.read())

                        txt_path = wav_out.replace(".wav", ".txt")

                        with open(txt_path, "w", encoding="utf-8") as f:
                            f.write(sentence.strip() + "\n") 
                    except:
                        continue

if __name__=='__main__':
    create_corpus_dir()