from sklearn import linear_model
clf = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
print clf.fit([[0,0], [0,0], [1,1]], [0,.1, 1])
print clf.alpha_