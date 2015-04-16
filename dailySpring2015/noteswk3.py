"""
processing fama french files 

create list - process list  

use the sum func. 

use len to get average 

##extra median value (use .sort() function  if even: average of two middle values.)




building containers

init 
loop 
filter/parse 
add to containers


list ordered mutable. 
tuple immutable 
set unordered. 
doct unordered
array type (everything must be the same type)

you are able to sort dics and sets 

duplicate values in a set get overwritten or ignored. 


"""

myset = set()
myset.add(5)
myset.add(10)
myset.add(5)
print myset
# will not print duplicates


mydict = {'a': 1, 'a':1}
print mydict
# only prints one time


"""
membership lookups

"""


intlist.append('hello')
# print intlist


# sets dont have an order so you need to use add instead of append. 

# .update() adds dics together. 

userId, name, lname, city, sate = line.split()

# splits by value in column

# .dir(int) .dir(str) .dir(set) ...

for line in open('students.txt'):
	userId, name = line.split
	ids_ name[userId] = filename

# fama order mkt_rf


days[year] = days[year] + mktrf 


myset = set(['a', 'b', 'c'])

if 'c' in myset:
	print "c is in myse"

years[year] = years[years] + mktrf
# will not work  

# use this 

if 'zzz' in mydict:
	print mydict['zzz']
else: 
	print 'key not found'

years.get('1927', 0)
years['1927']


try:
	print years['1928']
except KeyError:
	print "not found"
	days[year] = days[year] + mktrf 


sum()
len()
max()
min()

average = sum(mylist)/len(mylist)








































