from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD 
from numpy import array 

def parsePoint(line):
	values = [float(x) for x in line.replace(',', ' ').split(' ')]
	return LabeledPoint(values[0], values[1:])

data = sc.textFile("data/mllib/ridge-data/lpsa.data")
parsedData = data.map(parsePoint) 

model = LinearRegressionWithSGD.train(parsedData)

valuesAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
MSE = valuesAndPreds.map(lambda (v, p): (v - p)**2).reduce(lambda x, y: x + y) / valuesAndPreds.count()
print "Mean Squared Error = " +str(MSE)