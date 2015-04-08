#! usr/bin/env python 

threshold = 25 
mylist = [1, 43, 77, 4, 13, 8, 65, 11, 2]
# count = 0
newList = 0

for item in mylist:
	if item > threshold:
		newList += 1
print str(newList) + " elements of list are over the threshold of 25."
print "{0} elements of list are over the threshold of 25.".format(newList)