from sklearn import metrics
labels_true = [0, 0, 0, 1, 1, 1]
labels_pred = [0, 0, 1, 1, 2, 2]
# labels_pred = [1, 1, 0, 0, 3, 3]
labels_pred = labels_true[:]
# metrics.adjusted_rand_score(labels_true, labels_pred)
print metrics.adjusted_rand_score(labels_true, labels_pred)
print metrics.adjusted_mutual_info_score(labels_true, labels_pred)
print metrics.homogeneity_score(labels_true, labels_pred)
print metrics.completeness_score(labels_true, labels_pred)


