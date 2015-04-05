from sklearn.neighbors import NearestNeighbors 
from sklearn.neighbors.nearest_centroid import NearestCentroid 
import numpy as np 
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3,2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
print indices 
print distances
y = np.array([1, 1, 1, 2, 2, 2])
clf = NearestCentroid()
print clf.fit(X, y)
print(clf.predict([[-0.8, -1]]))