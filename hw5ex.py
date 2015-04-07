#! usr/bin/env python 

mylist = ['a', 'b', 'c', 'd', 'e']
counter = 0

for item in mylist:
	counter += 1

# print "mylist has " + str(counter) + " elements"

print 'mylist has {0} elements'.format(counter)