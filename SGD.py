from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = SGDClassifier(loss="hinge", penalty="l2")
print clf.fit(X, y)
print clf.predict([[2., 2.]])
print clf.coef_
print clf.intercept_ 
print clf.decision_function([[2., 2.]])
clf = SGDClassifier(loss='log').fit(X, y)
print clf.predict_ probab([[1., 1.]])


scaler = StandardScaler()
scaler.fot(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

