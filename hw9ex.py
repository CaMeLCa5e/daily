#! usr/bin/env python 

fixedwidth = [ 'abc123xyz',
 				'xxx000yyy',
 				'def987fed',
 				'zzz999zzz' ]
for item in fixedwidth:
	print item[3:6]

# this is tooooo much
	# slice = item[3:6]
	# print slice