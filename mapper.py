#! usr/bin/env python

import sys

for line in sys.stdin:
	# remove leading/trailing whitespace (why is this always the first step?  why would hadoop send data in separated lines?)
	line = line.strip()
	words = line.split()

	for word in words:
		print '%s\t%s' %(word, 1)

		