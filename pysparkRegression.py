from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array
 
def parsePoint(line):
	values = [float(x) for x in line.split(' ')]
	return LabeledPoint(values[0], values[1:])

data = sc.textFile("data/mllib/sample_svm_data.txt")
parsedData = data.map(parsePoint)

model = LogisticRegressionWithSGD.train(parsedData)

LabelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = LabelsAndPreds.filter(lambda (v, p): v != p).count() /float(parsedData.count())
print("trainingError =" + str(trainErr))