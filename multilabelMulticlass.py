# from sklearn.datasets import make_multilabel_classification
# from sklearn.preprocessing import MultiLabelBinarizer
# X, Y = make_multilabel_classification(n_samples=5, random_state=0, return_indicator=False)	

# print Y

# print MultiLabelBinarizer().fit_transform(Y)

from sklearn import datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
iris = datasets.load_iris()
X, y = iris.data, iris.target
print OneVsRestClassifier(LinearSVC(random_state=0)).fit(X, y).predict(X) 