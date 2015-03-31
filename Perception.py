"""
... needs import np statement 
For example, when dealing with boolean features, x_i^n = x_i for all n and is therefore useless; but x_i x_j represents the conjunction of two booleans. This way, we can solve the XOR problem with a linear classifier:
"""


from sklearn.linear_model import Perceptron
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = X[:, 0] ^ X[:, 1]
X = PolynomialFeatures(interaction_only=True).fit_transform(X)
print X
# array([[1, 0, 0, 0],
#        [1, 0, 1, 0],
#        [1, 1, 0, 0],
#        [1, 1, 1, 1]])
clf = Perceptron(fit_intercept=False, n_iter=10, shuffle=False).fit(X, y)
print clf.score(X, y)
