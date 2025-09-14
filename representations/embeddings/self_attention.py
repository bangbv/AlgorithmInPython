import torch, math



def seff_attention(X, d_model, dk):
    """
    Self-attention mechanism
    :param X: input tensor of shape (B, N, d_model)
    :return: output tensor of shape (B, N, d_model)
    """
    # Linear projections to Q, K, V
    WQ = torch.nn.Linear(d_model, dk, bias=False) # Query
    WK = torch.nn.Linear(d_model, dk, bias=False) # Key
    WV = torch.nn.Linear(d_model, dk, bias=False) # Value
    WO = torch.nn.Linear(dk, d_model, bias=False) # Output

    Q, K, V = WQ(X), WK(X), WV(X)                 # (B, N, dk)
    scores = Q @ K.transpose(-2, -1) / math.sqrt(dk)  # (B, N, N)
    weights = torch.softmax(scores, dim=-1) # (B, N, N)
    context = weights @ V                        # (B, N, dk)
    out = WO(context)                            # (B, N, d_model)
    return out

def embedding_sentence(sentence):
    # dictionary dc is restricted to the words that occur in the input sentence
    dc = {s:i for i,s in enumerate(sorted(sentence.replace(',', '').split()))}
    print(f"embedding_sentence:dictionary: {dc}")

    # we use this dictionary to assign an integer index to each word
    sentence_int = torch.tensor([dc[s] for s in sentence.replace(',', '').split()])
    print(f"embedding_sentence:sentence in integer: {sentence_int}")

    torch.manual_seed(123)
    embed = torch.nn.Embedding(6, 16)
    print(f"embedding_sentence:embedding matrix shape: {embed.weight.shape}")
    print(f"embedding_sentence:first row of embedding matrix: {embed.weight[0,:]}")

    embedded_sentence = embed(sentence_int).detach()
    return embedded_sentence

if __name__ == "__main__":
    sentences = [
        "hello world",  # len = 2
        "nice to meet you",  # len = 4
        "hello world again",  # len = 3
        "hello world again and again",  # len = 5
    ]

    B = 4  # batch size
    N = 10  # sequence length
    d_model = 512  # hidden size
    dk = d_model  # single head for simplicity


    # Generate random input tensor
    # torch.randn generates a tensor of random numbers from a normal distribution
    X = torch.randn(B, N, d_model)
    print(f"main: tensor of random number: shape: {X.shape}")
    # Format: matrix[depth, row, column]
    print(f"main: matrix at depth 0, row 0, column 0->5:\n{X[0, 0, 0:5]}")

    # Test the function
    embedded_sentence = embedding_sentence(X)
    print(f"main: embedded_sentence shape: {embedded_sentence.shape}")

    out = seff_attention(X, d_model, dk)
    print(f"main: out shape: {out.shape}")