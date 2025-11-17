import os
import json
import torchaudio
import torch
from torchaudio.compliance.kaldi import fbank
from tqdm import tqdm
json_dir = "json"
slurm_tmpdir = os.environ["SLURM_TMPDIR"]
# json_files = ["json/dev.json", "json/test.json", "json/train.json"]
splits = ["dev", "test", "train"]
for split in splits:
    json_file = f"json/{split}.json"
    with open(json_file, "r") as f:
        data = json.load(f)

    data_to_save = {}
    for key, value in tqdm(data.items()):
        wav_file = value["wav"]
        spk_id = value["spk_id"]
        phn = value["phn"]
        duration = value["duration"]
        filename = key.replace(".WAV", "").replace(spk_id+"_", "")
        # replace `/rds/project/rds-xyBFuSj0hm0/MLMI2.M2024/timit/` to slurm_tmpdir
        wav_file = wav_file.replace("/rds/project/rds-xyBFuSj0hm0/MLMI2.M2024/timit", slurm_tmpdir).lower()
        waveform, sample_rate = torchaudio.load(wav_file)
        feats = fbank(waveform)
        os.makedirs(os.path.join(slurm_tmpdir, "fbanks", spk_id), exist_ok=True)
        fbank_loc = os.path.join(slurm_tmpdir, "fbanks", spk_id, filename)
        torch.save(feats, fbank_loc)

        data_to_save[f"{spk_id}_{filename}"] = {
            "fbank": fbank_loc,
            "duration": duration,
            "spk_id": spk_id,
            "phn": phn,
        }
        
    with open(f"json/{split}_fbank.json", "w") as f:
        json.dump(data_to_save, f, indent=4)