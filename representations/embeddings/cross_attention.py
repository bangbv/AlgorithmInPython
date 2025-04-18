import torch, math
B, NT, NS, d_model = 16, 20, 30, 512
dk = d_model  # single head for simplicity

T = torch.randn(B, NT, d_model)   # target sequence
S = torch.randn(B, NS, d_model)   # source sequence

WQ = torch.nn.Linear(d_model, dk, bias=False)
WK = torch.nn.Linear(d_model, dk, bias=False)
WV = torch.nn.Linear(d_model, dk, bias=False)
WO = torch.nn.Linear(dk, d_model, bias=False)

Q = WQ(T)                          # (B, NT, dk)
K = WK(S)                          # (B, NS, dk)
V = WV(S)                          # (B, NS, dk)

scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(dk)  # (B, NT, NS)
weights = torch.softmax(scores, dim=-1)                        # (B, NT, NS)
context = torch.matmul(weights, V)                             # (B, NT, dk)

output = WO(context)                                           # (B, NT, d_model)
