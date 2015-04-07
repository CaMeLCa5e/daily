#! usr/bin/python

int1 = raw_input('please enter a number: ')
int2 = raw_input('please enter another number: ')
# the solution has a change to int(int1) but this step was unnecessary in my solution
if int1 < int2: 
	print '{0} is greater than {1}' .format(int1, int2)

elif int1 > int2:
	print '{0} is less than {1}' .format(int1, int2)

else: 
	print '{0} is equal to {0}' .format(int1, int2)