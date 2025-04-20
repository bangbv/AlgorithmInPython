import torch, math
B, N, d_model = 4, 10, 512   # batch, seq length, hidden size
dk = d_model                 # single head for simplicity

# torch.randn generates a tensor of random numbers from a normal distribution
X = torch.randn(B, N, d_model)
print(f"tensor of random number: shape: {X.shape}")
# Format: matrix[depth, row, column]
print(f"matrix at depth 0, row 0, column 0->5:\n{X[0, 0, 0:5]}")

# Linear projections to Q, K, V
WQ = torch.nn.Linear(d_model, dk, bias=False) # Query is same as input
WK = torch.nn.Linear(d_model, dk, bias=False) # Key is same as Query
WV = torch.nn.Linear(d_model, dk, bias=False) # Value is same as Query
WO = torch.nn.Linear(dk, d_model, bias=False) # Output is same as input

Q, K, V = WQ(X), WK(X), WV(X)                 # (B, N, dk)
scores = Q @ K.transpose(-2, -1) / math.sqrt(dk)  # (B, N, N)
weights = torch.softmax(scores, dim=-1) # (B, N, N)
context = weights @ V                        # (B, N, dk)
out = WO(context)                            # (B, N, d_model)

print(f"out shape: {out.shape}")
