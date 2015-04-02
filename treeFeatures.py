from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
print X.shape
clf = ExtraTreesClassifier()
X_new = clf.fit(X, y).transform(X)
print clf.feature_importances_
print X_new.shape


from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
print X.shape
# (150, 4)
clf = ExtraTreesClassifier()
X_new = clf.fit(X, y).transform(X)
print clf.feature_importances_  
# array([ 0.04...,  0.05...,  0.4...,  0.4...])
print X_new.shape               
# (150, 2)

