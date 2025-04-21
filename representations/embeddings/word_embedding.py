import torch
import torch.nn.functional as F

# source: https://sebastianraschka.com/blog/2023/self-attention-from-scratch.html
#
# embedding an input sentence
#
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


def weight_matrices(embedded_sentence):
    torch.manual_seed(123) # for reproducibility

    d = embedded_sentence.shape[1]
    print(f"weight_matrices:embedded_sentence shape d: {d}")

    d_q, d_k, d_v = 24, 24, 28

    W_query = torch.nn.Parameter(torch.rand(d_q, d))
    print(f"weight_matrices:W_query shape: {W_query.shape}")
    W_key = torch.nn.Parameter(torch.rand(d_k, d))
    print(f"weight_matrices:W_key shape: {W_key.shape}")
    W_value = torch.nn.Parameter(torch.rand(d_v, d))
    print(f"weight_matrices:W_value shape: {W_value.shape}")

    return W_query, W_key, W_value


def unnormalized_attention_weights(embedded_sentence, W_key, W_value):
    keys = W_key.matmul(embedded_sentence.T).T
    values = W_value.matmul(embedded_sentence.T).T

    print("unnormalized_attention_weights:key matrix:", keys.shape)
    print("unnormalized_attention_weights: values matrix:", values.shape)

    return keys, values


def attention_score(omega_2, d_k, values):
    attention_weights_2 = F.softmax(omega_2 / d_k ** 0.5, dim=0)
    print(attention_weights_2)

    context_vector_2 = attention_weights_2.matmul(values)

    print(context_vector_2.shape)
    print(context_vector_2)


if __name__ == "__main__":
    sentence = 'Life is short, eat dessert first'
    embedded_sentence = embedding_sentence(sentence)
    print(f"embedded sentence shape: {embedded_sentence.shape}")
    print(f"first row of embedded sentence: {embedded_sentence[0,:]}")
    W_query, W_key, W_value = weight_matrices(embedded_sentence)

    unnormalized_attention_weights(embedded_sentence, W_key, W_value)