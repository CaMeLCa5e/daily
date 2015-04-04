#!/usr/bin/env python

var = 5
var2 = 4

print var / float(var2)


int1 = raw_input('enter an int:')
int2 = raw_input('enter another:')

difference = int(int1) - int(int2)

print 'the difference between {0} and {1} is {2}'.format(int1, int2, difference)

# if int1 < int2:
# 	print '{0} is less than {1}'.format(int1, int2)

# elif int1 > int2:
# 	print '{0} is greater than {1}'.format(int1, int2)

# else:
# 	print '{0} is equal ton {1}'.format(int1, int2)

if not int1.isdigit():
	exit('first arg must be an int')

if not int2.isdigits():
	exit('second arg must be an int')

if not int1.isdigit() or not int2.isdigit():
	exit('both args must be ints')

int1 = int(int1)
int2 = int(int2)










