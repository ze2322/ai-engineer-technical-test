from transformers import BitsAndBytesConfig

bnb = BitsAndBytesConfig(

    load_in_4bit=True,

    bnb_4bit_quant_type="nf4",

    bnb_4bit_compute_dtype=torch.float16,

)

model = AutoModelForCausalLM.from_pretrained(

    MODEL,

    quantization_config=bnb,

    device_map="auto",

)