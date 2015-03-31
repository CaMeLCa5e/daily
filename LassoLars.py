from sklearn import linear_model
clf = linear_model.LassoLars(alpha=.1)
clf.fit([[0,0], [1,1]], [0, 1])
print clf.coef_