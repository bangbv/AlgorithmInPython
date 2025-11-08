
import torch
from transformers import BatchEncoding

# Method 1: Create BatchEncoding manually
def create_batch_encoding():
    batch_encoding = BatchEncoding({
        'input_ids': [[101, 2054, 2003, 1045, 102], [101, 1045, 2572, 102]],
        'attention_mask': [[1, 1, 1, 1, 1], [1, 1, 1, 1]],
        'token_type_ids': [[0, 0, 0, 0, 0], [0, 0, 0, 0]]
    })
    print(batch_encoding)
    return batch_encoding


def create_embedding(batch_encodding):
    # Create embedding matrix: [seq_len, 4] for the 4 components
    embedding = torch.tensor([
        batch_encodding
    ], dtype=torch.float32)

    print(f"embedding shape: {embedding.shape}")

if __name__ == "__main__":
    batch_encoding = create_batch_encoding()
    create_embedding(batch_encoding)