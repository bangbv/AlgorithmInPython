import numpy as np

# Create a sample 2D array (matrix)
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(f"matrix:{matrix}")

# Basic slicing: matrix[row_start:row_end, col_start:col_end]

# Get a single element
element = matrix[1, 2]  # Row 1, Column 2 (value: 7)
print(f"element row 1, column 2:{element}")

# Get an entire row
row = matrix[1, :]  # Second row [5, 6, 7, 8]
print(f"second row:{row}")

# Get an entire column
column = matrix[:, 2]  # Third column [3, 7, 11]
print(f"third column:{column}")

# Get a submatrix
submatrix = matrix[0:2, 1:3]  # Rows 0-1, Columns 1-2
# Result:
# [[2, 3],
#  [6, 7]]
print(f"submatrix rows 0-1, columns 1-2:{submatrix}")

# Strided slicing: matrix[row_start:row_end:row_step, col_start:col_end:col_step]
strided = matrix[::2, ::2]  # Every 2nd row and column
# Result:
# [[1, 3],
#  [9, 11]]
print(f"strided every 2nd row and column:{strided}")