import numpy as np

# Generating a random array
X = np.random.random((3, 5))  # a 3 x 5 array

print X


# get a single element
print X[0, 0]

# get a row
print X[1]

# get a column
print X[:, 1]

print X.T
