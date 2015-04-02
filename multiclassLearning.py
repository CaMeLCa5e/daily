# from sklearn import datasets
# from sklearn.multiclass import OutputCodeClassifier
# from sklearn.svm import LinearSVC
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
# clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=1)

# print clf.fit(X, y).predict(X)

from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
bagging = BaggingClassifier(KNeighborsClassifier(), max_samples=0.5, max_features=0.5)

print bagging