import numpy as np


def init_array():
    # Creating a 2D ndarray (matrix)
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr)
    return arr


def key_attributes(arr):
    ## 2.Key Attributes
    # The number of dimensions (axes) of the array
    print(arr.ndim)
    # The dimensions (size) of the array as a tuple. For a 2D array, it’s (rows, columns)
    print(arr.shape)
    # The total number of elements in the array.
    print(arr.size)
    # The data type of the elements in the array
    print(arr.dtype)
    # The size (in bytes) of each element in the array
    print(arr.itemsize)
    # The total number of bytes consumed by the elements of the array
    print(arr.nbytes)


def creating_arrays():
    ## 3.Creating Arrays
    # Creates an array of zeros with shape (2, 3)
    print(np.zeros((2, 3)))
    # Creates an array of ones with shape (3, 4)
    print(np.ones((3, 4)))
    # Creates a 3x3 identity matrix
    print(np.eye(3))
    # Creates an array of values starting from 0 to 9 with a step of 2
    print(np.arange(0, 10, 2))
    # Creates an array of 5 values evenly spaced between 0 and 1
    print(np.linspace(0, 1, 5))


## 4.Indexing and Slicing
def indexing_slicing():
    # Indexing: Accessing elements of the array using indices.
    arr = np.array([1, 2, 3, 4, 5])
    print(arr[2])  # Output: 3 (3rd element, 0-based index)
    # Slicing: Accessing sub-arrays using slices.
    print(arr[1:4])  # Output: [2 3 4] (elements from index 1 to 3)
    # Multi-dimensional indexing
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr_2d[1, 2])  # Output: 6 (element at row 1, column 2)


def broadcasting():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([[1], [2], [3]])
    # Here, arr1 is added to each row of arr2 due to broadcasting
    result = arr1 + arr2
    print(result)


def array_operations():
    # Element-wise Operations: Arithmetic operations (+, -, *, /) are performed element-wise.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    total  =  arr1 + arr2
    print(f"sum two arrays: {total}")  # Output: [5 7 9]
    # sum array with an arbitrary number
    total_2 = arr1 + 10
    print(f"sum array with an arbitrary number: {total_2}")  # Output: [11 12 13]
    # Aggregation Functions: sum, mean, max, min, etc.
    print(arr1.sum())  # Output: 6 (1 + 2 + 3)
    print(arr1.mean())  # Output: 2.0
    # Matrix Multiplication: Using the dot function or @ operator
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])
    print(np.dot(mat1, mat2))  # Matrix multiplication


# 7. Shape Manipulation
def shape_munipulation():
    # Reshaping: Changing the shape of an array
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.reshape(3, 2))
    # Transposing: Reversing or permuting the axes of an array
    print(arr.T)
    # Flatten: Converting a multi-dimensional array to a 1D array.
    print(arr.flatten())


if __name__ == '__main__':
    # arr = init_array()
    # key_attributes(arr)
    # creating_arrays()
    # indexing_slicing()
    # broadcasting()
    array_operations()
    # shape_munipulation()
