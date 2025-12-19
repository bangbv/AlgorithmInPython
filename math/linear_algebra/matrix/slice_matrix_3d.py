import numpy as np

# Create a 3D array (2 matrices of 3x4)
matrix_3d = np.array([
    # First matrix (index 0)
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    # Second matrix (index 1)
    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])
print(f"matrix_3d_shape:{matrix_3d.shape}")
print(f"matrix_3d:\n{matrix_3d}")
# Format: matrix[depth, row, column]

# Get a single element
element = matrix_3d[1, 0, 2]  # Depth 1, Row 0, Column 2 (value: 15)

# Get a complete 2D matrix at a specific depth
matrix_at_depth_0 = matrix_3d[0]  # First matrix
print(f"matrix_at_depth_0:\n{matrix_at_depth_0}")
matrix_at_depth_1 = matrix_3d[1]  # Second matrix

# Get a specific row across all depths
row_from_all = matrix_3d[:, 1, :]  # Row 1 from all depths
# Result:
# [[ 5,  6,  7,  8],
#  [17, 18, 19, 20]]

# Get a specific column across all depths
column_from_all = matrix_3d[:, :, 2]  # Column 2 from all depths
# Result:
# [[ 3,  7, 11],
#  [15, 19, 23]]

# Get a subcube
subcube = matrix_3d[0:2, 1:3, 1:3]
# Result:
# [[[ 6,  7],
#   [10, 11]],
#  [[18, 19],
#   [22, 23]]]