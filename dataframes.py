import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import svm, preprocessing 
import pandas as pd 
from matplotlib import style 
style.use("ggplot")

def Build_Data_Set(features = ["DE Ratio",
								"Trailing P/E"]):
	data_df = pd.DataFrame.from_csv("key_stats.csv")

	# data_df = data_df[:100]
	data_df = data_df.reindex()

	X = np.array(data_df[features].values.tolist())

	y = (data_df["Status"].replace("underperform", 0).replace("outperform",1).values.tolist())

	X = preprocessing.scale(X)


	return X, y

def Analysis():
	
	test_size = 500
	X, y = Build_Data_Set()
	print len(X)


	clf = svm.SVC(kernal = "linear", C=1.0)
	clf.fit(X,y)

	correct_count = 0

	for x in range(1, test_size+1):
		if clf.predict(X[-x])[0] == y[-x]:
			correct_count += 1

	print ("Accuracy:", (correct_count/test_size)*100.00)
	w = clf.coef_[0]

	a = -w[0] / w[1]

	xx = np/linspace(min(X[:, 0]), max(X[:, 0]))
	yy = a *xx - clf.intercept_[0]/w[1]

	h0 = plt.plot(xx,yy, "k-", label="non weighted")
	
	# x = [[1,3],
	# 	[1,5],
	# 	[1,7]
	# ]

	# X[:0]

	plt.scattered(X[:, 0],X[:, 1])
	plt.ylabel("Trailing P/E")
	plt.xlabel("DE Ratio")
	plt.legend()

	plt.show()

def Randomizing():
	df = pd.DataFrame({"D1":range(5), "D2":range(5)})
	print (df)
	df2 = df.reindex{np.random.permutation(df.index)}
	print (df2)



Randomizing()
# Analysis()






