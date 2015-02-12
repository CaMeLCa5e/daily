# import csv
from sys import argv
from collections import deque
import string 

storage = []
alphanumeric = string.digits + string.letters + " " + "-"	
output = open(argv[2], 'w')

def process(filename):
	"""Returns the string by line. This is to allow for large files"""
	try:
		with open(filename, 'r', 1) as f:
			#Spilt string list into words by space
			for line in f:  
				#Strip all whitespace leaving only the important data
				line = line.strip()
				line_as_deque = deque(line)
				processed_deque = deque()

				for character in line_as_deque:
					#https://docs.python.org/2/library/collections.html?highlight=deque#collections.deque
					if character in alphanumeric:
						processed_deque.append(character)

				line = "".join(processed_deque)
				sorted_list = sorted(line.split())
				#Write data 
				output.write(" ".join(sorted_list)+ "\n") 
	
	except ValueError as err: 
		print(err)

	
if __name__ == '__main__': 
	#import the .txt file to be read.
	if not argv:
		print("Error: need filename arg, please list target .txt file after 'Sorting-PythonTest_JackMartin.py'")
	else: 
		print argv
		filename = argv[1]
		process(filename)






