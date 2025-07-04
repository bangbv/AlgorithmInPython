import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from huggingface_hub import login
from transformers import pipeline

def login_huggingface():
    login(new_session=False)


def get_model_id():
    model_id = "meta-llama/Meta-Llama-3-8B"

    # Set up quantization config for efficient loading
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    return model_id, bnb_config


def load_model(model_id, bnb_config):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto" # Automatically maps layers to available devices (GPU/CPU)
    )
    return model, tokenizer


def get_generator(model, tokenizer):
    # You can now use the model for inference
    # For example, using a pipeline:
    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16, # Use bfloat16 for better performance on compatible GPUs
        device_map="auto"
    )
    return generator


if __name__ == "__main__":
    login_huggingface()
    # model_id, bnb_config = get_model_id()
    # model, tokenizer = load_model(model_id, bnb_config)
    # generator = get_generator(model, tokenizer)
    # prompt = "What is the capital of France?"
    # result = generator(prompt, max_new_tokens=50, num_return_sequences=1)
    # print(result[0]['generated_text'])