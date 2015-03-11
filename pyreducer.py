#! /usr/bin/env python

import sys

#map words to their count
foundKey = ""
foundValue = ""
isFirst = 1
currentCount = 0
currentCountry2digit = "-1"
currentCountryName = "-1"
isCountryMappingLine = False

for line in sys.stdin:
	line = line.strip()

	try:
		currentCountry2digit, personType, personName, countryName = line.split('^')

		if personName == "-1": 
			currentCountryName = countryName
			currentCountry2digit = currentCountry2digit
			isCountryMappingLine = True
		else:
			isCountryMappingLine = False

		if not isCountryMappingLine:

			if currentCountry2digit != country2digit:
				currentCountry2digit = country2digit
				currentCountryName = '%s - Unknown Country' %currentCountry2digit

			currentKey = '%s\t%s' % (currentCountryName, personType)

			if foundKey != currentKey: 
				if isFirst == 0:
					print '%s\t%s' % (foundKey,currentCount)
					currentCount = 0 
				else:
					isFirst = 0

				foundKey = currentKey

			currentCount += 1

	except:
		pass

try: 
	print '%s\t%s' % (foundKey, currentCount)
except:
	pass
	







