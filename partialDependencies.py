"""
1.11.4.7.2. Partial dependence



error: this code throws error:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Python/2.7/site-packages/sklearn/ensemble/partial_dependence.py", line 233, in plot_partial_dependence
    import matplotlib.pyplot as plt
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/pyplot.py", line 29, in <module>
    from matplotlib.figure import Figure, figaspect
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/figure.py", line 36, in <module>
    from matplotlib.axes import Axes, SubplotBase, subplot_class_factory
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/axes.py", line 20, in <module>
    import matplotlib.dates as _  # <-registers a date unit converter
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/dates.py", line 119, in <module>
    from dateutil.rrule import (rrule, MO, TU, WE, TH, FR, SA, SU, YEARLY,
  File "/Library/Python/2.7/site-packages/dateutil/rrule.py", line 14, in <module>
    from six.moves import _thread
ImportError: cannot import name _thread


>>> from sklearn.datasets import make_hastie_10_2
>>> from sklearn.ensemble import GradientBoostingClassifier
>>> from sklearn.ensemble.partial_dependence import plot_partial_dependence

>>> X, y = make_hastie_10_2(random_state=0)
>>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
...     max_depth=1, random_state=0).fit(X, y)
>>> features = [0, 1, (0, 1)]
>>> fig, axs = plot_partial_dependence(clf, X, features) 

"""



from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble.partial_dependence import plot_partial_dependence

X, y = make_hastie_10_2(random_state=0)
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X, y)
features = [0, 1, (0, 1)]
>>> fig, axs = plot_partial_dependence(clf, X, features) 
print fig, axs = plot_partial_dependence(clf, X, features)

