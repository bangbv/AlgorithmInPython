import torch, math

def multi_head_attention(X, Wq, Wk, Wv, Wo, num_heads, mask=None):
    B, N, d_model = X.shape
    d_k = d_model // num_heads

    Q = X @ Wq       # B × N × (h·d_k)
    K = X @ Wk
    V = X @ Wv

    # split heads
    def split(t):                            # (B, N, h, d_k) -> (B, h, N, d_k)
        return t.view(B, N, num_heads, d_k).transpose(1, 2)
    Q, K, V = map(split, (Q, K, V))

    scores = (Q @ K.transpose(-2, -1)) / math.sqrt(d_k)  # B × h × N × N
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))

    weights = torch.softmax(scores, dim=-1)
    C = weights @ V                                   # B × h × N × d_k
    C = C.transpose(1, 2).contiguous().view(B, N, d_model)

    return C @ Wo                                     # final projection
