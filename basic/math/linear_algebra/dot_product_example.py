import numpy as np

# vector x: [1, 2]
x = np.array([1,2])
# vector y: [3, 4]
y = np.array([3,4])
print(f"matrix x:\n{x}")
print(f"matrix y:\n{y}")
# Dot product
# The dot product of two vectors x and y is calculated as:
# x[0]*y[0] + x[1]*y[1]
dot_product = np.dot(x, y)  # or x @ y
print(f"Dot product of x and y: {dot_product}")