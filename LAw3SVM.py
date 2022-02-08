from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(n_samples=150, centers=2, random_state=42)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()  # plot initial values

from sklearn.svm import SVC

clf = SVC(kernel='linear')
clf.fit(X, y)  # train the classifier

y_pred = clf.predict(X)  # make predictions for same dataset


# method to create grid from scipy docs
def make_meshgrid(x, y, h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    print(xx.shape, yy.shape)
    return xx, yy


def plot_contours(clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = plt.contourf(xx, yy, Z, **params)
    return out


xx, yy = make_meshgrid(X[:, 0], X[:, 1])  # creates grid to plot in
plot_contours(clf, xx, yy, alpha=0.2, cmap=plt.cm.coolwarm)  # plots colored areas
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)  # plos actual dots
plt.show()  # shows everything together