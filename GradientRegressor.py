"""
1.11.4.2. Regression

import np is not used

http://scikit-learn.org/stable/modules/ensemble.html
"""

# import numpy as np 

from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_friedman1
from sklearn.ensemble import GradientBoostingRegressor

X, y = make_friedman1(n_samples=1200, random_state=0, noise=1.0)
X_train, X_test = X[:200], X[200:]
y_train, y_test = y[:200], y[200:]
est = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0, loss='ls').fit(X_train, y_train)
# print mean_squared_error(y_test, est.predict(X_test))

# _ = est.set_params(n_estimators=200, warm_start=True)
# _ = est.fit(X_train, y_train)
# print mean_squared_error(y_test, est.predict(X_test))

_ = est.set_params(n_estimators=200, warm_start=True)  # set warm_start and new nr of trees
_ = est.fit(X_train, y_train) # fit additional 100 trees to est
print mean_squared_error(y_test, est.predict(X_test))  



