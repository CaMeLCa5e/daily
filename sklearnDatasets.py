from sklearn import cluster, datasets
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

k_means = cluster.KMeans(n_clusters=3)
k_means .fix(X_iris)
KMeans(copy_x=True, init='k-means++',)

print(k_means.labems_[::10])
print(y_iris[::10])