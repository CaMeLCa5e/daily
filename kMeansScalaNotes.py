"""developed by amplab 
classifiation 
regression 
collab filtering 
clustering 
optomization 
dimentionality reduction 

sparse matricies 
"""

# data = sc.textFile('kmeans_data.txt')
# parsedData = data.map(.split('').map(toDouble))

# clusters = KMeans.train(parsedData, 5, numIterations = 20)

# cost = clusters.computeCost(parsedData)
# print "sum of squared errors = " + cost


# load and parse data 
data = sc.textFile("kmeans_data.txt")
parsedData = data.map(lambda line:
	array([float(x) for x in line.split(' ')])).cache()

#build the model
clusters = KMeans.train(parsedData, 5,maxIterations = 20,
	runs = 1, initialization_mode = "kmeans||")

#evaluate clustering by computing the sum of squared errors
def error(point):
	center = clusters.centers[clusters.predict(point)]
	return sqrt(sum([x**2 for x in (point - center)]))

cost = parsedData.map(lambda point: error(point))
	.reduce(lambda x, y: x + y)
	
print ("Sum of squared error = " + str(cost))









