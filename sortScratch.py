#! /usr/bin/python

from sys import argv

def process(filename):
	for string in filename:
		print sorted(string)


if __name__ == '__main__': 
	del argv[0]
	if not argv:
		print("Error: need filename arg, please list target .txt file before Sorting-PythonTest_JackMartin.py ")
	else:
		filename = argv[0]
		print process(input)