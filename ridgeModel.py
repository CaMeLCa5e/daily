from sklearn import linear_model
clf = linear_model.Ridge (alpha = .5)
print clf.fit([[0,0], [0,0], [1,1]], [0, .1, 1])
print clf.coef_
print clf.intercept_
