import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_circles



# ----------------- Feature Maps -----------------

# define a feature map that will map the 2d data into 3d dimension
# we can see that the formula is: (x, y) -> (x, y, x^2 + y^2)
def feature_map_1(X):
    return np.asarray((X[:, 0], X[:, 1], X[:, 0] ** 2 + X[:, 1] ** 2)).T



# define a feature RFB map that will map the 2d data into 3d dimension
# we can see that the formula is: (x, y) -> (x, y, x^2 + y^2)
def feature_map_2(X):
    return np.asarray((X[:,0], X[:,1], np.exp(-( X[:,0]**2 + X[:,1]**2)))).T


# define another polynomial feature map that will map the 2d data into 3d dimension
# we can see that the formula is: (x, y) -> (sqrt(2) * x * y, x^2, y^2)
def feature_map_3(X):
    return np.asarray(( np.sqrt(2) * X[:, 0] * X[:, 1], X[:, 0]**2, X[:, 1]**2)).T

# -------------------------------------------------



# ----------------- Create Data -----------------
def create_data(feature_map):
    # Create the dataset of two circles
    # y is the variable that will be used to separate the two circles
    """
    When using a numpy array we can filter the data using a condition, in our
    case we have a 1d array of 0s and 1s called y, with the same number of elements
    as the number of rows in X. So when we use X[rows, cols], we can use a condition
    to filter the rows that satify the condition. For example, if we want to filter
    the rows of X that have a 0 in the same index of y, we can use X[y == 0, :]. This
    will return all the rows of X that have a 0 in the same index of y. The same can
    be done for the 1s. This is a very powerful feature of numpy arrays.
    """

    X, y = make_circles(100, factor=0.18, noise=0.18, shuffle=True, random_state=0)
    Z = feature_map(X)
    X = np.asarray(X)
    condition_0 = y == 0
    condition_1 = y == 1
    return X, Z, condition_0, condition_1
# -------------------------------------------------



# ----------------- Plot Data -----------------
def plot_data(X, Z, condition_0, condition_1, title_2):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0] = fig.add_subplot(121)
    ax[0].scatter(X[condition_0, 0], X[condition_0, 1], color="red")
    ax[0].scatter(X[condition_1, 0], X[condition_1, 1], color="blue")
    ax[0].set_title("Original Data")

    # Now the 3d plot, the third column is the feature map
    ax[1] = fig.add_subplot(122, projection="3d")
    ax[1].scatter(Z[condition_0, 0], Z[condition_0, 1], Z[condition_0, 2], color="red")
    ax[1].scatter(Z[condition_1, 0], Z[condition_1, 1], Z[condition_1, 2], color="blue")
    ax[1].set_title(title_2)
# -------------------------------------------------




def main():
    X_1, Z_1, p1condition_0, p1condition_1 = create_data(feature_map_1)
    plot_data(X_1, Z_1, p1condition_0, p1condition_1, "Polynomial Map Data")

    # Now the RBF feature map, at the same time that the above plot
    X_2, Z_2, rfbcondition_0, rfbcondition_1 = create_data(feature_map_2)
    plot_data(X_2, Z_2, rfbcondition_0, rfbcondition_1, "RFB Map Data")

    X_3, Z_3, p2condition_0, p2condition_1 = create_data(feature_map_3)
    plot_data(X_3, Z_3, p2condition_0, p2condition_1, "Second Polynomial Map Data")
    plt.show()




if __name__ == '__main__':
    main()

