#!/usr/bin/python
import os 
import sys import argv
import csv

def process(filename):
	"""takes a data argument and processes duplicate and connected arguments"""
	with open(filename, 'r', 1) as f:
		total = []

	#raise exceptions, process matching 
		for row in csv.reader():
			if ValueError as err:
				print (err)
			else:
				return total

if __name__ == 'main':
	del argv[0]
	if not argv:
		print("Error: need filename arg")
	else:
		filename = argv[0]
		print process(filename)