import torch
import torch.nn as nn

# 𝐹(𝑥)=𝑚𝑎𝑥(0,𝑥)

relu = nn.ReLU(inplace=False)  # set inplace=True to save memory
x = torch.tensor([-2.0, -0.5, 0.0, 1.2, 3.4])
y = relu(x) # forward pass
print(f"relu(x): {y}")
