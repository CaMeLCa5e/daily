#! usr/bin/env python

""" This program is meant to accept 2 variables, multiply 
exponentially and return a value.  There should be appropriate top
and bottom borders on the return value.  

Here are two runs of the program (bold is user input):
$ python homework_2.py
please enter an integer: 3
please enter another integer: 14
=======
4782969
=======
$ python homework_2.py
please enter an integer: 3
please enter another integer: 5
===
243
===
"""


print "Please enter an integer:" 
basenumber = raw_input()

	
print "Please enter another integer:" 
exponent = raw_input()

final_value = int(basenumber) ** int(exponent)

bar_len = len(str(final_value))
#final_value is an int so it needs to be changed to 
#a string before it can be processed.

final_bar = bar_len * "="


print final_bar
print final_value
print final_bar

