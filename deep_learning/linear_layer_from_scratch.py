import torch
import torch.nn as nn

class MyLinear(nn.Module):
    def __init__(self, in_dim, out_dim, bias=True):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_dim, in_dim) * (2 / in_dim)**0.5)
        if bias:
            self.bias = nn.Parameter(torch.zeros(out_dim))
        else:
            self.register_parameter('bias', None)

    def forward(self, x):
        # x: [batch_size, in_dim]
        # self.weight: [out_dim, in_dim]
        # result: [batch_size, out_dim]
        y = x.matmul(self.weight.t())
        if self.bias is not None:
            y += self.bias
        return y


layer  = MyLinear(8, 3)
dummy  = torch.randn(5, 8)   # batch of 5 samples, 8 features each
out    = layer(dummy)
print(out.shape)             # torch.Size([5, 3])
out.sum().backward()         # gradients now populated
print(layer.weight.grad.shape)  # torch.Size([3, 8])
