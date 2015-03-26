from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degre=3, gamma=0.0,
kernel="rbf", max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0])

print y[0]
