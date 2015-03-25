import numpy as np 


from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


accuracy = clf.score(features_test, labels_test)
"""
accuracy = no. of points classified correctly/ all points
method 1 = write code that compares predictions to y_test, element by element

"""
# GaussianNB()

# print(clf.predict([-.8, -1]))