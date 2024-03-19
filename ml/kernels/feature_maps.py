from typing import Any

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_circles


# define a feature map that will transform the 2d data into 3d data
# we can see that the formula is: (x, y) -> (x, y, x^2 + y^2)
def feature_map_1(X):
    return np.asarray((X[:, 0], X[:, 1], X[:, 0] ** 2 + X[:, 1] ** 2)).T


def main():
    # Create the dataset of two circles
    X, y = make_circles(100, factor=0.15, noise=0.15, shuffle=True, random_state=0)


    Z = feature_map_1(X)
    X = np.asarray(X)

    # y is the target variable, we can use it to separate the data
    # of the two circles
    condition_0 = y == 0
    condition_1 = y == 1

    # with the make circles dataset, we can see that the data is not linearly separable
    # but with the feature map, we can see that the data is linearly separable
    # lets plot both the 2d  and the feature map data to see the difference,

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0] = fig.add_subplot(121)
    ax[0].scatter(X[condition_0, 0], X[condition_0, 1], color="red")
    ax[0].scatter(X[condition_1, 0], X[condition_1, 1], color="blue")
    ax[0].set_title("Original Data")

    # Now the 3d plot, the third column is the feature map
    ax[1] = fig.add_subplot(122, projection="3d")
    ax[1].scatter(Z[condition_0, 0], Z[condition_0, 1], Z[condition_0, 2], color="red")
    ax[1].scatter(Z[condition_1, 0], Z[condition_1, 1], Z[condition_1, 2], color="blue")
    ax[1].set_title("Feature Map Data")

    plt.show()

if __name__ == '__main__':
    main()
