#! /usr/bin/env python
import sys

for line in sys.stdin:
	try: 
		personName = '-1'
		personType = '-1'
		countryName = '-1'
		country2digit = '-1'

		line = line.strip()

		splits = line.split("|")

		if len(splits) == 2: #country data
			countryName = splits[0]
			country2digit = splits[1]
		else: 
			personName = splits[0]
			personType = splits[1]
			country2digit = splits[2]

		print '%s^%s^%s%s' % (country2digit, personType, personName, countryName)

	except: 
		pass

		