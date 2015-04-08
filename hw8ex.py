#! usr/bin/env python 

matchVar = raw_input("Please enter a match string ")
# matchVar = 'hello'
strlist = ['hello', 'me', 'you', 'mustard', 'hello', 'you', 'hello']
instance = 0

for item in strlist:
	if item == matchVar:
		instance += 1

# print instance

print '{0} instances of "'.format(instance)+ matchVar +'" in strlist'
# is this cheap? yes, yes it is.  Ps - is anyone going to DEFCON this year? 

matchvar = 'hello'
count = 0
for string in strlist:
	if string == matchvar:
		count += 1
print '{0} instances of "{1}" in strlist'.format(count, matchvar)