#! usr/bin/python

#locate value in a list
 
list =['a','e','i','o','u']
find = 'o'

pos = 0
found = False

while pos < len(list):
	if list[pos] == find:
		print(find."found at position:", pos)
		found = True
		break

	pos += 1

if found == False:
	print(find,'not found')