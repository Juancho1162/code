import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_circles



# ----------------- Feature Maps -----------------

# define a feature map that will map the 2d data into 3d dimension
# we can see that the formula is: (x, y) -> (x, y, x^2 + y^2)
def feature_map_1(D):
    return np.asarray((D[:, 0], D[:, 1], D[:, 0] ** 2 + D[:, 1] ** 2)).T



# define a feature RFB map that will map the 2d data into 3d dimension
# we can see that the formula is: (x, y) -> (x, y, x^2 + y^2)
def feature_map_2(D):
    return np.asarray((D[:,0], D[:,1], np.exp(-( D[:,0]**2 + D[:,1]**2)))).T


# define another polynomial feature map that will map the 2d data into 3d dimension
# we can see that the formula is: (x, y) -> (sqrt(2) * x * y, x^2, y^2)
def feature_map_3(D):
    return np.asarray(( np.sqrt(2) * D[:, 0] * D[:, 1], D[:, 0]**2, D[:, 1]**2)).T

# -------------------------------------------------



# ----------------- Create Data -----------------
def create_data(feature_map):
    # Create the dataset of two circles
    # y is the variable that will be used to separate the two circles
    """
    When using a numpy array we can filter the data using a condition, in our
    case we have a 1d array of 0s and 1s called y that classifies our dataset in two groups
    with the same number of elements as the number of rows in X. So when we use 
    X[rows, cols], we can use a condition to filter the rows that satify the condition.
    For example, if we want to filter the rows of X that have a 0 in the same index of y,
    we can use X[y == 0, :].
    
    This will return all the rows of X that have a 0 in the same index of y. The same can
    be done for the 1s. This is a very powerful feature of numpy arrays.
    """

    D, y = make_circles(100, factor=0.18, noise=0.18, shuffle=True, random_state=0)
    mapped_D = feature_map(D)
    D = np.asarray(D)
    condition_0 = y == 0
    condition_1 = y == 1
    return D, mapped_D, condition_0, condition_1, y
# -------------------------------------------------



# ----------------- Plot Data -----------------
def plot_data(D, mapped_D, condition_0, condition_1, title_2):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0] = fig.add_subplot(121)
    ax[0].scatter(D[condition_0, 0], D[condition_0, 1], color="red")
    ax[0].scatter(D[condition_1, 0], D[condition_1, 1], color="blue")
    ax[0].set_title("Original Data")

    # Now the 3d plot, the third column is the feature map
    ax[1] = fig.add_subplot(122, projection="3d")
    ax[1].scatter(mapped_D[condition_0, 0], mapped_D[condition_0, 1], mapped_D[condition_0, 2], color="red")
    ax[1].scatter(mapped_D[condition_1, 0], mapped_D[condition_1, 1], mapped_D[condition_1, 2], color="blue")
    ax[1].set_title(title_2)
# -------------------------------------------------




def main():
    D_1, mapped_D_1, p1condition_0, p1condition_1, y_1 = create_data(feature_map_1)
    plot_data(D_1, mapped_D_1, p1condition_0, p1condition_1, "Polynomial Map Data")

    # Now the RBF feature map, at the same time that the above plot
    D_2, mapped_D_2, rfbcondition_0, rfbcondition_1, y_2 = create_data(feature_map_2)
    plot_data(D_2, mapped_D_2, rfbcondition_0, rfbcondition_1, "RFB Map Data")

    D_3, mapped_D_3, p2condition_0, p2condition_1, y_3 = create_data(feature_map_3)
    plot_data(D_3, mapped_D_3, p2condition_0, p2condition_1, "Second Polynomial Map Data")
    plt.show()


if __name__ == '__main__':
    main()

