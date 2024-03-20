import numpy as np
from feature_maps import *
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.datasets import make_circles
from sklearn.metrics import accuracy_score

# ----------------- Kernel -----------------
# we are going to define a kernel function using our feature maps
# from the feature_maps.py file

"""
The kernel parameter in svm.SVC expects a function that takes two data points (vectors) and returns a scalar value representing the kernel evaluation between those two data points. My mapped data has a shape of (100,3) and the function kernel
 should have a shape of 
"""

# Here X and Y are the data points that we want to evaluate the kernel function
def kernel_1(X, Y): 
    return np.dot(feature_map_1(X), feature_map_1(Y).T)

def kernel_2(X, Y):
    return np.dot(feature_map_2(X), feature_map_2(Y).T)

def kernel_3(X, Y):
    return np.dot(feature_map_3(X), feature_map_3(Y).T)





# -------------------------------------------------

# ----------------- Create Data -----------------
X_1, Z_1, p1condition_0, p2condition_1, y_1 = create_data(feature_map_1)
X_2, Z_2, rfbcondition_0, rfbcondition_1, y_2 = create_data(feature_map_2)
X_3, Z_3, p3condition_0, p3condition_1, y_3 = create_data(feature_map_3)
# -------------------------------------------------


# ----------------- Train SVM -----------------

# we are going to train the SVM with the kernel function
clf_1 = svm.SVC(kernel=kernel_1)
clf_2 = svm.SVC(kernel=kernel_2)
clf_3 = svm.SVC(kernel=kernel_3)

# we are going to fit the SVM with the data
clf_1.fit(X_1, y_1)
clf_2.fit(X_2, y_2)
clf_3.fit(X_3, y_3)

# Calculate the accuracy of the model
y_pred_1 = clf_1.predict(X_1)
y_pred_2 = clf_2.predict(X_2)
y_pred_3 = clf_3.predict(X_3)

"""
print("Accuracy of the model with feature map 1: ", accuracy_score(y_1, y_pred_1))
print("Accuracy of the model with feature map 2: ", accuracy_score(y_2, y_pred_2))
print("Accuracy of the model with feature map 3: ", accuracy_score(y_3, y_pred_3))
"""
# -------------------------------------------------

# ----------------- Plot Data, and decision boundary -----------------

def plot_data_and_decision_boundary(X, Z, condition_0, condition_1, clf, title):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0] = fig.add_subplot(121)
    ax[0].scatter(X[condition_0, 0], X[condition_0, 1], color="red")
    ax[0].scatter(X[condition_1, 0], X[condition_1, 1], color="blue")
    ax[0].set_title("Original Data")

    # Now the 3d plot, the third column is the feature map
    ax[1] = fig.add_subplot(122, projection="3d")
    ax[1].scatter(Z[condition_0, 0], Z[condition_0, 1], Z[condition_0, 2], color="red")
    ax[1].scatter(Z[condition_1, 0], Z[condition_1, 1], Z[condition_1, 2], color="blue")
    ax[1].set_title(title)

    # Plot the decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax[0].contourf(xx, yy, Z, alpha=0.4)

def main():
    plot_data_and_decision_boundary(X_1, Z_1, p1condition_0, p2condition_1, clf_1, "Polynomial Map Data")
    plot_data_and_decision_boundary(X_2, Z_2, rfbcondition_0, rfbcondition_1, clf_2, "RBF Map Data")
    plot_data_and_decision_boundary(X_3, Z_3, p3condition_0, p3condition_1, clf_3, "Second Polynomial Map Data")
    plt.show()



if __name__ == "__main__":
    main()
