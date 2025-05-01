import numpy as np

def one_hot(idx, size):
    out = np.zeros((size, 1))
    out[idx] = 1.0
    return out


def forward(inputs, h_prev):
    """
    inputs : list of one-hot column vectors length T
    h_prev : (hidden_size, 1) state from previous batch
    returns: loss, cache needed for back-prop
    """
    xs, hs, ys, ps = {}, {}, {}, {}
    hs[-1] = h_prev
    loss = 0.0

    for t, x_t in enumerate(inputs):
        xs[t] = x_t
        hs[t] = np.tanh(W_xh @ x_t + W_hh @ hs[t-1] + b_h)
        ys[t] = W_hy @ hs[t] + b_y
        ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t]))
        target_idx = np.argmax(inputs[t+1])          # next char
        loss += -np.log(ps[t][target_idx, 0])

    cache = (xs, hs, ps)
    return loss / len(inputs), hs[len(inputs)-1], cache


def backward(cache, h_last, inputs):
    xs, hs, ps = cache
    # gradients initialised to zero
    dW_xh, dW_hh, dW_hy = [np.zeros_like(m) for m in (W_xh, W_hh, W_hy)]
    db_h  = np.zeros_like(b_h)
    db_y  = np.zeros_like(b_y)
    dh_next = np.zeros_like(h_last)

    for t in reversed(range(len(inputs)-1)):
        dy = ps[t].copy()
        target_idx = np.argmax(inputs[t+1])
        dy[target_idx] -= 1      # dL/dy
        dW_hy += dy @ hs[t].T
        db_y  += dy

        dh = W_hy.T @ dy + dh_next          # back-prop into h
        dh_raw = (1 - hs[t]**2) * dh        # tanh'
        dW_xh += dh_raw @ xs[t].T
        dW_hh += dh_raw @ hs[t-1].T
        db_h  += dh_raw
        dh_next = W_hh.T @ dh_raw

    # clip to mitigate exploding gradients
    for dparam in (dW_xh, dW_hh, dW_hy, db_h, db_y):
        np.clip(dparam, -5, 5, out=dparam)

    return dW_xh, dW_hh, dW_hy, db_h, db_y


def sgd(params, grads, lr):
    for p, g in zip(params, grads):
        p -= lr * g


def sample(seed_char, length=50, vocab_size=0):
    h = np.zeros((hidden_size, 1))
    x = one_hot(stoi[seed_char], vocab_size)
    out = [seed_char]

    for _ in range(length):
        h = np.tanh(W_xh @ x + W_hh @ h + b_h)
        y = W_hy @ h + b_y
        p = np.exp(y) / np.sum(np.exp(y))
        idx = np.random.choice(range(vocab_size), p=p.ravel())
        x = one_hot(idx, vocab_size)
        out.append(itos[idx])
    return "".join(out)


# main function
if __name__ == "__main__":
    # load data
    text = "hello world\n"
    chars = sorted(set(text))
    vocab_size = len(chars)

    # mapping tables
    stoi = {c: i for i, c in enumerate(chars)}
    itos = {i: c for c, i in stoi.items()}

    # hyper-parameters
    np.random.seed(42)
    hidden_size = 32      # neurons in hidden state
    seq_length   = 5      # time steps to unroll
    lr           = 1e-1   # learning rate

    # weight initalisation
    W_xh = np.random.randn(hidden_size, vocab_size) * 0.01
    W_hh = np.random.randn(hidden_size, hidden_size) * 0.01
    b_h  = np.zeros((hidden_size, 1))

    W_hy = np.random.randn(vocab_size, hidden_size) * 0.01
    b_y  = np.zeros((vocab_size, 1))

    # training loop
    h_prev = np.zeros((hidden_size, 1))

    for epoch in range(500):
        # prepare a training sequence of length seq_length+1
        idx = epoch % (len(text) - seq_length - 1)
        seq = text[idx: idx + seq_length + 1]
        inputs = [one_hot(stoi[ch], vocab_size) for ch in seq]  # T = seq_length+1

        loss, h_prev, cache = forward(inputs[:-1], h_prev)
        grads = backward(cache, h_prev, inputs)
        sgd([W_xh, W_hh, W_hy, b_h, b_y], grads, lr)

        if epoch % 50 == 0:
            print(f"epoch {epoch:3d} | loss {loss:.3f}")

    print(sample(chars, 40, vocab_size))