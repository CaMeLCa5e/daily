from sklearn import linear_model
X = [[0., 0.], [1., 1.], [2.,2.], [3., 3.]]
Y = [0., 1., 2., 3.]
clf = linear_model.BayesianRidge()
print clf.fit(X, Y) 