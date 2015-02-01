import csv 

with open('input1.txt') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

	for row in readCSV:
		print row