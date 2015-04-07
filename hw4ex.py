#! usr/bin/env python 

int1 = raw_input('please enter a digit ')
int2 = raw_input('please enter another digit ')

if not int1.isdigit() or not int2.isdigit():
	exit('both arguments must be an integer')

if int1 < int2: 
	print '{0} is greater than {1}' .format(int1, int2)

elif int1 > int2:
	print '{0} is less than {1}' .format(int1, int2)

else: 
	print '{0} is equal to {0}' .format(int1, int2)