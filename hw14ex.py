#! /usr/bin/env python

contact_list = [ 'George:Hartwell:NY\n',
 				 'Mary:Jones:NJ\n',
 				 'Sue:Baker:PA\n',
 				 'Hani:Ali:NJ\n',
				 'Gwen:Meyers:NJ\n',
 				 'Druge:Gerrold:NY\n' ]

input = raw_input('Please enter requested state abbreviation')
input = input.upper()
result_count = 0

print 'individuals in {0}:' .format(input)

for line in contact_list:
	line = line.rstrip()
	els = line.split(':')
	if els[-1] == input:
		print "{0} {1}" .format(els[0], els[1])
		result_count += 1

if result_count == 0:
	print 'no results found for {0}'.format(input)
	# print els[-1]

