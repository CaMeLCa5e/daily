from math import exp 
import sys 

import numpy as np 
from pyspark import SparkContext 
from pyspark.mllib.regression import LabeledPoint 
from pyspark.mllib.classification import LogisticRegressionWithSGD 

def parsePoint(line):
	values = [float(s) for s in line.split(' ')]
	if values[0] == -1:
		values[0] = 0
	return LabeledPoint(values[0], values[1:])

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print >> sys.stderr, "Usage: logistic_regression <file> <iterations>"
		exit(-1)
	sc = SparkContext(appName="PythonLR")
	points = sc.textFile(sys.argv[1].map(parsePoint)
	iterations = int(sys.argv[2])
	model = LogisticRegressionWithSGD.train(points, iterations)
	print "Final weights: " + str(model.weights)
	print "Final intercept: " + str(model.intercept)
	sc.stop()
	