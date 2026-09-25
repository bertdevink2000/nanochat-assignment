import json
from pathlib import Path

import matplotlib.pyplot as plt


root = Path(__file__).resolve().parents[1]
rows = {}
for line in (root / "report" / "task2_metrics.jsonl").read_text().splitlines():
    item = json.loads(line)
    rows.setdefault(item["step"], {}).update(item)

steps = [step for step, row in sorted(rows.items()) if "train/bpb" in row]
plt.plot(steps, [rows[x]["train/bpb"] for x in steps], label="Training")
plt.plot(steps, [rows[x]["val/bpb"] for x in steps], label="Validation")
plt.xlabel("Training step")
plt.ylabel("Bits per byte")
plt.legend()
plt.tight_layout()
plt.savefig(root / "report" / "task2_bpb.png", dpi=200)
