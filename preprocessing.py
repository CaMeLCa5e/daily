from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline 
model = Pipeline([('poly', PolynomialFeatures(degree=3)), 
					('linear', LinearRegression(fit_intercept=False))])

x = np.arange(5)
y = 3 - 2 * x + x ** 2 - x ** 3
model = model.fit(x[:, np.newaxis], y)
model