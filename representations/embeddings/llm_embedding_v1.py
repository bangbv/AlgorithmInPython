import torch
from transformers import GPT2Model



batch_size = 2
seq_len = 10  # sequence length
hidden_dim = 768  # GPT-2 hidden dimension
model = GPT2Model.from_pretrained("gpt2")

# PyTorch example
embedding_vectors = torch.randn(batch_size, seq_len, hidden_dim)  # your pre-computed embeddings

# Feed directly to transformer blocks (skipping the token embedding)
outputs = model(inputs_embeds=embedding_vectors)

print(outputs.shape)