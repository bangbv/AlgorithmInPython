import torch

# source: https://sebastianraschka.com/blog/2023/self-attention-from-scratch.html
# embedding an input sentence
sentence = 'Life is short, eat dessert first'
# dictionary dc is restricted to the words that occur in the input sentence
dc = {s:i for i,s in enumerate(sorted(sentence.replace(',', '').split()))}
print(f"dictionary: {dc}")

# we use this dictionary to assign an integer index to each word
sentence_int = torch.tensor([dc[s] for s in sentence.replace(',', '').split()])
print(f"sentence in integer: {sentence_int}")


torch.manual_seed(123)
embed = torch.nn.Embedding(6, 16)
embedded_sentence = embed(sentence_int).detach()

print(embedded_sentence)
print(embedded_sentence.shape)
