import numpy as np
from scipy.optimize import minimize, rosen

def _f(x):
    f = 5 * x ** 4 - 4 * x ** 3 + 3 * x ** 2 - 2
    return f

x_0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(_f, 0.01)

print(res.x)
