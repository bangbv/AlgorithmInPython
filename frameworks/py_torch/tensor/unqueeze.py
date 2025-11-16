import torch

# Original embeddings tensor with shape (sequence_length, embedding_dim)
embeddings = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
print(f"embeddings.shape:{embeddings.shape}")  # torch.Size([3])
print(f"embeddings result: {embeddings}")

# After unsqueeze(0)
embeddings_batched = embeddings.unsqueeze(0)
print(f"embeddings_batched.shape: {embeddings_batched.shape}")  # torch.Size([1, 3])
print(f"embeddings_batched: {embeddings_batched}")