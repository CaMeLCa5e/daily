from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import os
import pydot

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

with open("iris.dot", 'w') as f:
	f = tree.export_graphviz(clf, out_file=f)

os.unlink('iris.dot')
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")

print clf.predict(iris.data[:1, :])
print clf.predict_proba(iris.data[:1, :])

X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
print clf.predict([[1, 1]])
