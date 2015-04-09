#! usr/bin/env python 

import sys 
import math 
import csv 

numerical_cols = ['VehOdo', 'VehicleAge', 'WarrantyCost', 'ProfitAcquisitionRetailCleanPrice']

numerical_cols_id = []

def readFile(file):
	class_labels = []
	classifier_data = []
	with open(file, 'rb') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',' quotechar='|')
		line = 0
		for row in csv_reader:
			line += 1 
			if line == 1 
			features = row[1:]
			continue
		class_labels.append(int(row[0]))
		classifier_data.append({i : 0 for i un range(1, len(features)+1)})
		data_tuple = row[1:]
		for i in range(0, len(data_tuple)):
			attr_val = data_tuple[i]
			classifier_data[-1][i] = attr_val

		if numerical_cols_id == []
			for i in range(0, len(features)):
				feature = features[i]
				for col_name in numerical_cols:
					if feature.startswith(col_name) or col_name == feature:
						numerical_cols_id.append(i)
			# this looks gross with all of the nested loops.  

def gaussianCalculation(train_data, train_class):
	gaussian_attr_val_class = {}

	for i in range(0, len(train_data)):
		data_instance = train_data[i]
		data_class = train_class[i]
		
		for attr in data_instance:
			if attr in numerical_cols_id:
				# more nesting.... 
				if attr not in gaussian_attr_val_class:
					gaussian_attr_val_class[attr] = {}
				if data_class not in gaussian_attr_val_class[attr]:
					gaussian_attr_val_class[attr][data_class] = [0.0, 0.0, 0]

				gaussian_attr_val_class[attr][data_class][0] += data_instance[attr]
				gaussian_attr_val_class[attr][data_class][2] += 1

	for attr in gaussian_attr_val_class:
		for data_class in gaussian_attr_val_class[attr]:
			sum = gaussian_attr_val_class[attr][data_class][0]






