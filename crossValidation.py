"""
Cross-validation
http://scikit-learn.org/stable/modules/cross_validation.html
import np statement is unnecessary
"""
# import numpy as np 
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
iris.data.shape, iris()