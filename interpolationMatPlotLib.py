import matplotlib.pyplot as plt 

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100)

print(len(digits.data))

x,y = digits.data[:-3], digits.target[:-3]
clf.fit(x,y)

print('Prediction:', clf.predict(digits.data[-7]))

plt.imshow(digits.images[-7], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()