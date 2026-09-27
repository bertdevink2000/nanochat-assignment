import argparse
import json
import os

from nanochat.checkpoint_manager import load_model
from nanochat.common import autodetect_device_type, compute_cleanup, compute_init
from nanochat.engine import Engine


parser = argparse.ArgumentParser()
parser.add_argument("--model-tag", default="task3-sft")
parser.add_argument("--step", type=int, default=None)
parser.add_argument("--output", default="report/task4_samples.json")
parser.add_argument("--max-tokens", type=int, default=128)
args = parser.parse_args()

device_type = autodetect_device_type()
_, _, _, _, device = compute_init(device_type)
model, tokenizer, _ = load_model(
    "sft", device, phase="eval", model_tag=args.model_tag, step=args.step
)
engine = Engine(model, tokenizer)

prompts = [
    "Why is the sky blue? Answer in two sentences.",
    "A train travels at 60 km/h for 2.5 hours. How far does it travel?",
    "Write a four-line poem about rain on a city street.",
    "Give three practical tips for reducing food waste.",
    "Leg in het Nederlands uit waarom bladeren groen zijn.",
]
temperatures = [0.1, 0.7, 1.5]
rows = []

for i, prompt in enumerate(prompts):
    conversation = {
        "messages": [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": ""},
        ]
    }
    tokens = tokenizer.render_for_completion(conversation)
    for temperature in temperatures:
        generated, _ = engine.generate_batch(
            tokens,
            max_tokens=args.max_tokens,
            temperature=temperature,
            top_k=50,
            seed=42 + i,
        )
        answer = tokenizer.decode(generated[0][len(tokens):]).strip()
        rows.append({
            "prompt": prompt,
            "temperature": temperature,
            "response": answer,
        })
        print(f"\nTemperature {temperature} | {prompt}\n{answer}")

os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
with open(args.output, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

compute_cleanup()
