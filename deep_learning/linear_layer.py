import torch
import torch.nn as nn
import numpy as np

lin = nn.Linear(in_features=128, out_features=64, bias=True)
x   = torch.randn(32, 128)  # [batch_size, in_features]
y   = lin(x)                # y = x·Wᵀ+b  ➜  shape (32,64)

print(f"input x shape: {x.shape}")
print(f"input y shape: {y.shape}")
print(f"three rows of input x: {np.array2string(x[0:2,0:5].numpy(), precision=2)}")
print(f"three rows of output y: {np.array2string(y[0:2,0:5].detach().numpy(), precision=2)}")


"""
What happens inside:
forward(x):
    y = x @ W.T     # matrix multiply, shape (batch, out)
    if bias: y += b
W and b are registered as nn.Parameters; 
their gradients are tracked automatically during back‑propagation.
"""