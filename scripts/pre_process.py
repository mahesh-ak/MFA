import os
import tarfile
import csv
from pathlib import Path
import soundfile as sf
from tqdm import tqdm

root = "fleurs/data"
out_root = "processed_data"

def create_corpus_dir():
    N = len(os.listdir(root))
    for i, lang_dir in enumerate(os.listdir(root)):
        print(f"processing {lang_dir} ({i+1}/{N})")
        lang_path = os.path.join(root, lang_dir)
        if not os.path.isdir(lang_path):
            continue

        tsv_path = os.path.join(lang_path, "train.tsv")
        tar_path = os.path.join(lang_path, "audio", "train.tar.gz")
        if not (os.path.exists(tsv_path) and os.path.exists(tar_path)):
            continue

        out_dir = os.path.join(out_root, lang_dir, "textgrid_corpus_directory")
        vocab_path = os.path.join(out_root, lang_dir, "vocab.txt")
        Path(out_dir).mkdir(parents=True, exist_ok=True)

        vocab = []
        entries = {}

        # Load TSV entries: filename → (sentence, cleaned_chars)
        with open(tsv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)
            for row in reader:
                wav_name = row[1]
                word_col = row[3]              # characters separated by spaces
                text_for_textgrid = " ".join(word_col.split())   # join by space
                cleaned = word_col.split()              # for vocab.txt
                entries[wav_name] = (text_for_textgrid, cleaned)
                vocab.extend(cleaned)

        # Extract wavs and create TextGrids
        with tarfile.open(tar_path, "r:gz") as tar:
            for member in tqdm(tar.getmembers()):
                name = os.path.basename(member.name)
                if name in entries:
                    wav_out = os.path.join(out_dir, name)
                    with tar.extractfile(member) as src, open(wav_out, "wb") as dst:
                        dst.write(src.read())

                    audio, sr = sf.read(wav_out)
                    duration = len(audio) / sr

                    sentence, _ = entries[name]
                    tg_path = wav_out.replace(".wav", ".TextGrid")

                    with open(tg_path, "w", encoding="utf-8") as tg:
                        tg.write(
                            "File type = \"TextGrid\"\n"
                            "Object class = \"TextGrid\"\n\n"
                            f"xmin = 0\nxmax = {duration}\n"
                            "tiers? <exists>\nsize = 1\nitem []:\n"
                            "    item [1]:\n"
                            "        class = \"IntervalTier\"\n"
                            "        name = \"1\"\n"
                            "        xmin = 0\n"
                            f"        xmax = {duration}\n"
                            "        intervals: size = 1\n"
                            "        intervals [1]:\n"
                            "            xmin = 0\n"
                            f"            xmax = {duration}\n"
                            f"            text = \"{sentence}\"\n"
                        )

        # Write vocabulary
        with open(vocab_path, "w", encoding="utf-8") as f:
            for w in sorted(set(vocab)):
                f.write(w + "\n")