import torch
import torch.nn.functional as F

# source: https://sebastianraschka.com/blog/2023/self-attention-from-scratch.html
#
# embedding an input sentence
#
def self_attention(sentence):
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

    query = W_query.matmul(embedded_sentence.T).T
    keys = W_key.matmul(embedded_sentence.T).T
    values = W_value.matmul(embedded_sentence.T).T
    omega = query.matmul(keys.T)

    print("unnormalized_attention_weights:key matrix:", keys.shape)
    print("unnormalized_attention_weights: values matrix:", values.shape)
    print(f"omega shape: {omega.shape}")
    print(f"omega 2nd column: {omega[1, :]}")

    x_2 = embedded_sentence[1]
    query_2 = W_query.matmul(x_2)
    key_2 = W_key.matmul(x_2)
    value_2 = W_value.matmul(x_2)
    omega_24 = query_2.dot(keys[4])
    print(f"omega_24: {omega_24}")

    omega_2 = query_2.matmul(keys.T)
    print(f"omega_2: {omega_2}")

    attention_weights = F.softmax(omega / d_k ** 0.5, dim=0)
    attention_weights_2 = F.softmax(omega_2 / d_k ** 0.5, dim=0)
    print(f"attention_weights_2: {attention_weights_2}")
    print(f"attention_weights shape: {attention_weights.shape}")
    print(f"attention_score:{attention_weights}")

    context_vector = attention_weights.matmul(values)

    print(context_vector.shape)
    # print(f"context_vector 2nd row: {context_vector[:,:]}")

    return context_vector


if __name__ == "__main__":
    sentence = 'Life is short, eat dessert first'
    self_attention(sentence)

