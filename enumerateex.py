days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
	print day


for index, day in enumerate(days):
	print "days[{0}] contains {1}".format(index, day)
	print "day contains {0}".format(day)

for index, day in enumerate(days):
	print "{0} is day # {1}".format(day, index+1)