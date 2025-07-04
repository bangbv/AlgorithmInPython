import torch
import numpy as np

# link: https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
# Initializing a Tensor
def init_tensor():
    # Directly from data
    data = [[1, 2],[3, 4]]
    x_data = torch.tensor(data)
    print(f"Directly from data: {x_data}")
    # From a NumPy array
    np_array = np.array(data)
    x_np = torch.from_numpy(np_array)
    print(x_np)
    # From another tensor
    x_ones = torch.ones_like(x_data)  # retains the properties of x_data
    print(f"Ones Tensor: \n {x_ones} \n")
    x_rand = torch.rand_like(x_data, dtype=torch.float)  # overrides the datatype of x_data
    print(f"Random Tensor: \n {x_rand} \n")


def attribute_tensor():
    # Attributes of a Tensor
    tensor = torch.rand(3,4)
    print(f"Shape of tensor: {tensor.shape}")
    print(f"Datatype of tensor: {tensor.dtype}")
    print(f"Device tensor is stored on: {tensor.device}")


# operations on Tensors
def operations_tensor():
    # Directly from data
    data = [[1, 2],[3, 4]]
    tensor = torch.tensor(data)
    # We move our tensor to the GPU if available
    if torch.cuda.is_available():
        tensor = tensor.to("cuda")
    # Standard numpy-like indexing and slicing
    tensor = torch.ones(4, 4)
    print(f"First row: {tensor[0]}")
    print(f"First column: {tensor[:, 0]}")
    print(f"Last column: {tensor[..., -1]}")
    tensor[:, 1] = 0
    print(tensor)
    # Joining tensors
    t1 = torch.cat([tensor, tensor, tensor], dim=1)
    print(t1)
    # Arithmetic operations
    # This computes the matrix multiplication between two tensors. y1, y2, y3 will have the same value
    # ``tensor.T`` returns the transpose of a tensor
    y1 = tensor @ tensor.T
    y2 = tensor.matmul(tensor.T)

    y3 = torch.rand_like(y1)
    torch.matmul(tensor, tensor.T, out=y3)

    # This computes the element-wise product. z1, z2, z3 will have the same value
    z1 = tensor * tensor
    z2 = tensor.mul(tensor)

    z3 = torch.rand_like(tensor)
    torch.mul(tensor, tensor, out=z3)


if __name__ == "__main__":
    # init_tensor()
    # attribute_tensor()
    operations_tensor()