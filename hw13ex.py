#! /usr/bin/env python

contact_list = [ 'George:Hartwell:NY\n',
 				 'Mary:Jones:NJ\n',
 				 'Sue:Baker:PA\n',
 				 'Hani:Ali:NJ\n',
				 'Gwen:Meyers:NJ\n',
 				 'Druge:Gerrold:NY\n' ]

for line in contact_list:
	line = line.rstrip()
	els = line.split(':')
	print els[-1]