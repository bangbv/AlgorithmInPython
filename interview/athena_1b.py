import numpy as np

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_circles
from sklearn.preprocessing import StandardScaler

X, y = make_circles(n_samples=100, noise=0.05)

# scatter plot, dots colored by class value
# fig, ax = plt.subplots()
# ax.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()
def _f(X):
    x = StandardScaler().fit_transform(X)  # normalizing the features
    pca_wp = PCA(n_components=2)
    principal_components_wp = pca_wp.fit_transform(x)
    return principal_components_wp
Z = _f(X)

fig, ax = plt.subplots()
ax.scatter(Z[:, 0], Z[:, 1], c=y)
plt.show()
