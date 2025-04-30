import torch

vocab = {
    "<pad>": 0, "hello": 1, "world": 2, "nice": 3,
    "to": 4, "meet": 5, "you": 6, "again": 7
}
def encode(sentence):
    """Split on space & map each token to its int ID."""
    return [vocab[w] for w in sentence.split()]


sentences = [
    "hello world",          # len = 2
    "nice to meet you",     # len = 4
    "hello world again"     # len = 3
]
B = len(sentences)         # ⇒ 3


token_lists = [encode(s) for s in sentences]   # [[1,2], [3,4,5,6], [1,2,7]]
L = max(len(t) for t in token_lists)           # ⇒ 4 (max length)
for t in token_lists:                          # right-pad with 0 (<pad>)
    t += [0] * (L - len(t))
# token_lists → [[1,2,0,0],
#                [3,4,5,6],
#                [1,2,7,0]]
print(f"token_lists: {token_lists}")

batch_ids = torch.tensor(token_lists, dtype=torch.long)  # (3, 4)
print(f"batch_ids shape: {batch_ids.shape}")

d = 6                              # embedding dimension
embed = torch.nn.Embedding(len(vocab), d, padding_idx=0)

print(f"embed.weight shape: {embed.weight.shape}")

embedded_batch = embed(batch_ids)   # (3, 4, 6)
print(f"embedded_batch shape: {embedded_batch.shape}")
# torch.Size([3, 4, 6])
