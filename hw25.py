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

filename = "famaFrench.txt"
count = 0
sumOfFama = 0
total_line_mktrf = []

# Use raw_input() to take user input - a 4-digit year. 
year = raw_input('Please enter a 4-digit year: ')

# Reject the input with a polite message if it is not all digits. 
if not year.isdigit():
	exit('sorry, that was bad input')

for line in open('famaFrench.txt'):
    line = line.rstrip()
    line_words = line.split()
    line_year = line[0:4]

    if line_year == year: 
    	count += 1
    	print line_year

    	MktRF = line.split()[1:2]
    	line_mktrf = MktRF
    	print line_mktrf
    	total_line_mktrf = 
    	average_mktrf = print sum(total_line_mktrf)

total_line_mktrf.append(line_mktrf)

    	# total_line_mktrf = total_line_mktrf.rstrip()
    	# total_line_mktrf = total_line_mktrf.split()

    	# print sum(total_line_mktrf)
print total_line_mktrf

for line in line_year:
	if line_year == year:
		count += 1
		print count 

# print line

# sum - add the data together
	
# # average the sum and return as dec. 
# average = sumOfFama / float(count)

# # format = count 301, sum 26.26, avg 0.0872425249169
# print 'count {0}, sum {1}, avg {2}'.format(count, sumOfFama, average)
# print 'count %s, sum %d, avg %d' % (count, sumOfFama, average)

# print count
if count == 0:
	print 'no results found for requested year'

# for line in contact_list:
#  	line = line.rstrip()

 	# print "{0} {1}".format(els[0], els[1])
 	# result_count += 1


