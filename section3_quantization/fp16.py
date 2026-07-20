import json
import os
import time

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM



MODEL = "Qwen/Qwen2.5-1.5B-Instruct"
DEVICE = torch.device("cpu")

print("=" * 60)
print("Running FP16 Benchmark (CPU Mode)")
print("=" * 60)



tokenizer = AutoTokenizer.from_pretrained(MODEL)

model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    dtype=torch.float32,  # CPU doesn't support FP16 inference well
)

model.to(DEVICE)
model.eval()

with open(
    "section3_quantization/prompts.txt",
    "r",
    encoding="utf-8",
) as f:
    prompts = [line.strip() for line in f if line.strip()]

results = []


for prompt in prompts:

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
    ).to(DEVICE)

    start = time.time()

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
        )

    latency = time.time() - start

    generated_tokens = outputs.shape[1] - inputs.input_ids.shape[1]

    tokens_per_second = generated_tokens / max(latency, 1e-6)

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
    )

    results.append(
        {
            "prompt": prompt,
            "answer": answer,
            "latency_seconds": round(latency, 3),
            "generated_tokens": generated_tokens,
            "tokens_per_second": round(tokens_per_second, 2),
            "vram_gb": 0,
        }
    )


os.makedirs(
    "section3_quantization/output",
    exist_ok=True,
)

with open(
    "section3_quantization/output/fp16_results.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(
        results,
        f,
        indent=4,
        ensure_ascii=False,
    )

print("\nFinished FP16 Benchmark!")
print("Results saved to:")
print("section3_quantization/output/fp16_results.json")