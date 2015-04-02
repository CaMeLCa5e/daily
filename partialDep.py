# from sklearn.ensemble.partial_dependence import partial_dependence
# from sklearn.ensemble import GradientBoostingClassifier

# pdp, axes = partial_dependence(clf, [0], X=X)
# clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X, y)
# print pdp
# print axes

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble.partial_dependence import plot_partial_dependence

X, y = make_hastie_10_2(random_state=0)
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X, y)
features = [0, 1, (0, 1)]
fig, axs = plot_partial_dependence(clf, X, features) 