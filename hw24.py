#!/usr/bin/env python

"""
24. Use raw_input() to take two integers from the user (call raw_input() twice). 

Verify that they are all numbers; exit() with error if not. 
Divide one number into the other, and print the result. 
Ensure a floating-point result (e.g., 6/4 should be 1.5, not 1).

Expected output:
Please enter first integer: 6
Please enter second integer: 4
6 / 4 = 1.5
Please enter first integer: 6
Please enter second integer: hello
ERROR: part of your input is invalid -- two integers required.
"""


int1 = raw_input('please enter an int: ')
int2 = raw_input('please enter anoter int: ')


if not int1.isdigit():
	exit('first argument must be an integer')

if not int2.isdigit():
	exit('second argument must be an integer')

int1 = int(int1)
int2 = int(int2)

print '{0} / {1} = '.format(int1, int2) + str(float(int1)/int2)














