# source: https://docs.pytorch.org/docs/stable/tensors.html
import torch

def concat_tensors_test():
    # initialization
    x = [1, 2]
    y = [3, 4]
    tensor_x = torch.tensor(x)
    tensor_y = torch.tensor(y)
    # concatenation
    result = torch.cat((tensor_x, tensor_y), dim=0)

    print(f"result after concat tensor x and y: {result}")

def concat_tensors():
    """
    Concatenate two tensors along the specified dimension.
    """
    # Example tensors
    tensor_a = torch.tensor([[1, 2],[3,4]])
    tensor_b = torch.tensor([[5, 6, 7], [7, 8, 9]])
    print(f"tensor_a: {tensor_a}")
    print(f"tensor_b: {tensor_b}")
    print(f"tensor_a shape: {tensor_a.shape}")
    print(f"tensor_b shape: {tensor_b.shape}")

    # Concatenation along dimension 0 (rows)
    # result_dim0 = torch.cat((tensor_a, tensor_b), dim=0)
    # print(f"result_dim0: {result_dim0}")
    # print(f"tensor_a shape: {tensor_a.shape}")
    # Concatenation along dimension 1 (columns)
    result_dim1 = torch.cat((tensor_a, tensor_b), dim=1)
    print(f"result_dim1: {result_dim1}")
    print(f"tensor_b shape: {tensor_b.shape}")

    # return result_dim0, result_dim1


def key_broadcast():
    a = torch.tensor([[1], [2], [3]])  # 3x1
    b = torch.tensor([10, 20, 30])     # 1x3
    print(f"tensor a: {a}")
    print(f"tensor a shape: {a.shape}")
    print(f"tensor b: {b}")
    print(f"tensor b shape: {b.shape}")
    print(f"Broadcasting to 3x3")
    result = a + b  # Broadcasting to 3x3
    print(f"tensor result: {result}")
    print(f"result shape: {result.shape}")


if __name__ == "__main__":
    # concat_tensors()
    key_broadcast()
