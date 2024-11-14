import numpy as np
# The initial expression in a list comprehension can be any arbitrary expression,
# including another list comprehension.

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
np_matrix = np.array(matrix)
print(f"matrix: \n{np_matrix}")
# Transpose rows and columns
transpose = [[row[i] for row in matrix] for i in range(4)]
np_transpose = np.array(transpose)
print(f"transpose: \n{np_transpose}")