from sklearn.preprocessing import PolynomialFeatures
import numpy as np 
X = np.arange(6).reshape(3, 2)
print X

poly = PolynomialFeatures(degree=2)
print poly.fit_transform(X)
