import numpy as np

class Embedding:
    def __init__(self, vocab_size, d, padding_idx=None, seed=0):
        rng = np.random.default_rng(seed)
        self.W = rng.normal(0, 0.02, size=(vocab_size, d)).astype(np.float32)
        self.padding_idx = padding_idx
        self._grad = np.zeros_like(self.W)

    def forward(self, token_ids):
        """
        token_ids: np.int64 array of shape (B, T)
        returns: embeddings of shape (B, T, d)
        """
        self.last_ids = token_ids  # needed for backward
        out = self.W[token_ids]    # fancy indexing: gather rows
        return out

    def zero_grad(self):
        self._grad.fill(0.0)

    def backward(self, dOut):
        """
        dOut: gradient from upper layer, shape (B, T, d)
        Accumulate into self._grad for only the used rows.
        """
        Batch, length, dim = dOut.shape # batch size = 1, sequence length, embedding dim
        # T, d = dOut.shape # sequence length, embedding dim
        ids = self.last_ids.reshape(-1)       # (B*T,)
        dOut_flat = dOut.reshape(Batch*length, dim)      # (B*T, d)
        # dOut_flat = dOut.reshape(T, d)      # (B*T, d)

        # Accumulate gradients per token id
        np.add.at(self._grad, ids, dOut_flat)

        # Don't update padding row (optional)
        if self.padding_idx is not None:
            self._grad[self.padding_idx] = 0.0

    def step(self, lr=1e-2):
        self.W -= lr * self._grad

if __name__ == "__main__":
    # --- tiny demo ---
    V, dim = 10, 4 # vocab size, embedding dim
    emb = Embedding(V, dim, padding_idx=0)
    token_ids = np.array([[1, 2, 3], [4,5,6]], dtype=np.int64)   # (B=2, T=3)
    print(f"input token ids: {token_ids}")
    E = emb.forward(token_ids)                     # (2,3,4)
    print(f"forward: embeddings E shape: {E.shape}")
    print(f"forward: embeddings E: {E}")
    loss = E.sum()  # silly loss, just for demo
    print(f"loss: {loss}")
    dE = np.ones_like(E)  # d(loss)/dE = 1
    print(f"dE: {dE}")
    print(f"dE shape: {dE.shape}")

    emb.zero_grad() # clear previous gradient
    emb.backward(dE)  # fills emb._grad only at used rows
    emb.step(lr=0.1) # update weights
    print(f"updated embedding matrix:{emb.W}")
