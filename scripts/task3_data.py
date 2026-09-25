import json

from tasks.gsm8k import GSM8K
from tasks.mmlu import MMLU
from tasks.smoltalk import SmolTalk


datasets = {
    "MMLU": MMLU(subset="all", split="auxiliary_train"),
    "GSM8K": GSM8K(subset="main", split="train"),
    "SmolTalk": SmolTalk(split="train"),
}
for name, dataset in datasets.items():
    print(f"{name}: {len(dataset):,} rows")
    for i in range(3):
        print(json.dumps(dataset[i], ensure_ascii=False, indent=2))
