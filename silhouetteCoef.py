"""
Silhouette Coefficient

http://scikit-learn.org/stable/modules/clustering.html#clustering

2.3.9.4. Silhouette Coefficient 

"""


from sklearn import metrics 
# # from sklearn.metrics import pairwise_distances
from sklearn import datasets
# import numpy as np 
# from sklearn.cluster import KMeans
dataset = datasets.load_iris()
X = dataset.data 
y = dataset.target 

# kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
# print metrics.silhouete_score(X, labels, metric='euclidean')

# import numpy as np (this is unncessary)
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
labels = kmeans_model.labels_
print metrics.silhouette_score(X, labels, metric='euclidean')
