import numpy as np

# A = np.array([[1., 2, 3, 2], [4, 3, 7, 4], [1, 4, 2, 3]])
# print(A)
# print("np.sum:", np.sum(A, axis=0))
# print("np.min:", np.min(A, axis=0))

A = np.array([[1., 5], [2, 3]])
B = np.array([[5., 8], [7, 3]])
print("A:", A)
print("B:", B)
print("A*B:", A*B)
print("A.dot(B):",A.dot(B))