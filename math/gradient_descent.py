import numpy as np

def embedding_backward(token_ids, dE, vocab_size, d, padding_idx=None, dtype=np.float32):
    """
    Compute dL/dW for an embedding lookup:
      E = W[token_ids]    # forward
    Given dE = dL/dE (same shape as E), return grad_W = dL/dW.

    Args:
        token_ids: (B, T) int64 array
        dE:        (B, T, d) float array (upstream grad wrt E)
        vocab_size: int
        d:          int (embedding dim)
        padding_idx: int or None
    Returns:
        grad_W: (vocab_size, d) float array
    """
    # 1) Allocate gradient buffer
    grad_W = np.zeros((vocab_size, d), dtype=dtype)

    # 2) Flatten indices and gradients
    ids = token_ids.reshape(-1)      # (B*T,)
    dE_flat = dE.reshape(-1, d)      # (B*T, d)

    # 3) Scatter-add: accumulate per token id
    #    np.add.at handles repeated indices correctly.
    np.add.at(grad_W, ids, dE_flat)

    # 4) Optional: don't update padding row
    if padding_idx is not None:
        grad_W[padding_idx] = 0.0

    return grad_W


def numerical_grad(f, W, eps=1e-5):
    grad = np.zeros_like(W)
    it = np.nditer(W, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        old = W[idx]
        W[idx] = old + eps
        fpos = f(W)
        W[idx] = old - eps
        fneg = f(W)
        W[idx] = old
        grad[idx] = (fpos - fneg) / (2*eps)
        it.iternext()
    return grad


if __name__ == "__main__":
    # Example: loss = sum(E) where E = W[token_ids]
    rng = np.random.default_rng(0)
    V, d = 7, 3 # vocab size, embedding dim
    W = rng.normal(0, 0.1, size=(V, d)).astype(np.float32) # embedding matrix
    token_ids = np.array([[1, 3, 4],
                        [5, 6, 7]], 
                        dtype=np.int64)

    # Upstream gradient dE for loss = sum(E) is ones
    dE = np.ones((2, 3, d), dtype=np.float32) # (B=2, T=3, d)

    # Analytic gradient
    grad_analytic = embedding_backward(token_ids, dE, V, d, padding_idx=None)

    # Numerical gradient
    def loss_fn(Wparam):
        E = Wparam[token_ids]  # gather
        return E.sum()         # scalar

    grad_numeric = numerical_grad(loss_fn, W.copy())

    # They should match (small tolerance due to finite diff)
    print(np.allclose(grad_analytic, grad_numeric, atol=1e-6))

