import csv
import operator 

sample = open('input1.txt', 'r')

sample2 = [(), (), ()]

sort = sorted(sample2,key=operator.itemgetter(0))

for eachline in sort:
	print eachline

	