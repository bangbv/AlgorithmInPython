import numpy as np

x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print("x", x)
print("y", y)
z = np.around(np.dot(x,y)).astype(int)
print("z", z)
print(np.dot(y,z))
# lambda_add_numbers = lambda a, b: a + b
# print(lambda_add_numbers(3, 4))
#
# filled_list = [a/2 for a in range(10)]
# print(filled_list)

# a = np.array([[1, 2], [2, 2]])
# b = np.array([2, 2, 2])
# print(a.shape)
# print(b.shape)
# c = np.dot(a, b)
# d = np.multiply(a, b)
# e = np.cross(a,b)
# f = np.linalg.solve(a)
# print(c)
# print(d)
# print(e)
# print(f)


