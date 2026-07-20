import json

with open("section3_quantization/output/fp16_results.json") as f:
    fp16 = json.load(f)

with open("section3_quantization/output/int4_results.json") as f:
    int4 = json.load(f)

print("=" * 70)
print("FP16 vs INT4")
print("=" * 70)

for i in range(len(fp16)):
    print(f"\nPrompt {i+1}")
    print("-" * 70)

    print(fp16[i]["prompt"])

    print(f"\nFP16")
    print(f"Latency : {fp16[i]['latency']} s")
    print(f"Speed   : {fp16[i]['tokens_per_second']} tokens/s")
    print(f"VRAM    : {fp16[i]['vram']} GB")

    print(f"\nINT4")
    print(f"Latency : {int4[i]['latency']} s")
    print(f"Speed   : {int4[i]['tokens_per_second']} tokens/s")
    print(f"VRAM    : {int4[i]['vram']} GB")