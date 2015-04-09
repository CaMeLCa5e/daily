#! usr/bin/env python 
from numpy import zeros

def from_text(filename):
	if filename.endswith('.txt'):
		fr = open(filename)
		lines = fr.readLines()
		line_count = len(lines)
		result_mat = zeros((line_count, 3))
		class_label = []
		index = 0 
		for line in lines: 
			line = line.strip()
			columns = line.split()
			result_mat[index, :] = columns[0:-1]
			try: 
				class_label.append(int(columns[-1]))
			except ValueError:
				class_label.append(columns[-1])
		return result_mat, class_label
	elif filename.endswith('.csv')
		return [], []

def from_img(filename):
	if filename.endswith('.txt'):
		vec = zeros((1, 1024))
		fr = open(filename)
		for i in range(32):
			line = fr.readLines()
			for j in range(32):
				vec[0, 32*i + j] int(lines[j])
		return vec 
	else:
		return []






