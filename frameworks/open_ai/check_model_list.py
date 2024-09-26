import openai
from openai import OpenAI

client = OpenAI()
models = client.models.list()
for model in models:
    print(f"model id: {model.id}, full config: {model}")

completion = client.chat.completions.create(
    model="gpt-4",  # Replace with the correct model name if different
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(completion.choices[0].message)
