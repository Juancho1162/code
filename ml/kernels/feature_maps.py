import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_circles


def feature_map_1(X):
    return np.asarray((X[:, 0], X[:, 1], X[:, 0] ** 2 + X[:, 1] ** 2)).T


X, y = make_circles(100, factor=0.1, noise=0.1, shuffle=True, random_state=0)
Z = feature_map_1(X)



# with the make circles dataset, we can see that the data is not linearly separable
# but with the feature map, we can see that the data is linearly separable
# lets plot both the 2d  and the feature map data to see the difference,
# puting the correct labels on the plot

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0] = fig.add_subplot(121)
ax[0].scatter(X[y==0, 0], X[y==0, 1], color='red')
ax[0].scatter(X[y==1, 0], X[y==1, 1], color='blue')
ax[0].set_title('Original Data')

# Now the 3d plot, the third column is the feature map
ax[1] = fig.add_subplot(122, projection='3d')
ax[1].scatter(Z[y==0, 0], Z[y==0, 1], Z[y==0, 2], color='red')
ax[1].scatter(Z[y==1, 0], Z[y==1, 1], Z[y==1, 2], color='blue')
ax[1].set_title('Feature Map Data')

plt.show()
