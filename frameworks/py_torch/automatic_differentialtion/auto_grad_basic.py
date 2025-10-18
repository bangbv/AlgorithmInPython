# source: https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html
import torch

# Tensors, Functions and Computational graph
input = torch.ones(5)  # input tensor
print(f"input: {input}")
expected_output = torch.zeros(3)  # expected output
print(f"expected_output: {expected_output}")
w = torch.randn(5, 3, requires_grad=True) # weight matrix
print(f"weight matrix w: {w}")
bias = torch.randn(3, requires_grad=True) # bias vector
print(f"bias vector bias: {bias}")
actual_output = torch.matmul(input, w)+bias # actual output
print(f"actual output matrix: {actual_output}")
loss = torch.nn.functional.binary_cross_entropy_with_logits(actual_output, expected_output)
print(f"loss = {loss}")

# Computing Gradients
final_output = loss.backward() # backpropagate the loss
print(f"final output: {final_output}") # None
