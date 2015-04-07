#! usr/bin/env python
"""
25. Use raw_input() to take user input - a 4-digit year. 

Reject the input with a polite message if it is not all digits. 

Looping through the Fama-French_data.txt file, calculate the average MktRF value for that year.


program runs with expected output:

$ python 2-25.py
please enter a 4-digit year: hello
sorry, that was bad input

$ python 2-25.py
please enter a 4-digit year: what's wrong?
sorry, that was bad input

$ python 2-25.py
please enter a 4-digit year: 1990
count 253, sum -12.77, avg -0.0504743083004

$ python 2-15.py
please enter a 4-digit year: 1927
count 301, sum 26.26, avg 0.0872425249169

$ python 2-15.py
please enter a 4-digit year: 1945
count 286, sum 32.55, avg 0.113811188811
"""
int1 = raw_input('Please enter a 4-digit year: ')

if not int1.isdigit():
	exit('sorry, that was bad input')

# elif not int1 == len(4):
	# exit('argument must be a 4 character integer')






