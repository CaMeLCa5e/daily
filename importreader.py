import csv 
with open('input1.txt') as csvfile:
	filereader = csv.reader(csvfile)
	for row in filereader:
		print ' '.join(row)

