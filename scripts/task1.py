import subprocess
import sys
from pathlib import Path

from nanochat.common import get_base_dir
from nanochat.tokenizer import RustBPETokenizer


samples = {
    "english": "A small language model learns patterns from text, but careful evaluation still matters.",
    "numbers": "Invoice 2026-0917 totals 12,345.67 euros; item 0042 costs 98.50.",
    "code": "def cube_sum(n):\n    return sum(k ** 3 for k in range(1, n + 1))",
    "dutch": "De trein naar Leiden vertrekt om kwart over acht vanaf spoor negen.",
}

out = Path(get_base_dir()) / "task1"
subprocess.run([sys.executable, "-m", "nanochat.dataset", "-n", "3"], check=True)
print("vocab_size,sample,characters,tokens,tokens_per_character")

for size in (8192, 32768):
    spot = out / str(size)
    subprocess.run([
        sys.executable, "-m", "scripts.tok_train",
        "--max-chars", "500000000",
        "--vocab-size", str(size),
        "--output-dir", str(spot),
    ], check=True)

    tok = RustBPETokenizer.from_directory(spot)
    for name, text in samples.items():
        pieces = len(tok.encode(text))
        print(f"{size},{name},{len(text)},{pieces},{pieces / len(text):.4f}")
