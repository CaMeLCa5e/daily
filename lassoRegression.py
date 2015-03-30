from sklearn import linear_model
clf = linear_model.Lasso(alpha = 0.1)
print clf.fit([[0, 0], [1, 1]], [0,1])
