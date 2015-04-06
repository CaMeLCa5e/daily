from sklearn.learning_curve import learning_curve
from sklearn.svm import SVC 
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
# X, y = X[indices], y[indices]


train_sizes, train_scores, valid_scores = learning_curve(SVC(kernel='linear'), X, y, train_sizes=[50, 80, 110], cv=5)
print train_sizes
print train_scores
print valid_scores