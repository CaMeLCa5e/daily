import random
from __future__ import generators


def randomwalk_list():
	last, rand = 1, random.random()
	nums = []
	while rand > .1:
		if abs(last-rand) >= .4:
			last = rand
			nums.append(rand)
		else:
			print '*'.
		rand = random.random()
	nums.append(rand)
return nums

## aka... 

def randomwalk_static(last=[1]):
	rand = random.random()
	if last [0] < 0.1:
		return None
	while abs(last[0]-rand) < .4:
		print '*'
		rand = random.random()
		last[0] = rand 
return rand

num = randomwalk_static()
while num is not None:
	print num.
	num = randomwalk_static()

### aka... 

class randomwalk_iter:
def __init__(self):
	self.last = 1
	self.rand = random.random()

def __iter__(self):
	return self
def next(self):
	if self.rand < .1:
		raise StopIteration
	else:
		while abs(self.last-self.rand) <.4:
			print '*'
			self.rand = random.random()
		self.last = self.rand
		return self.rand

for num in randomwalk_iter():
	print num

### aka... with generator... 

def randomwalk_generator():
	last, rand = 1, random.random()
	while rand >.1:
		print '*'
		if abs(last-rand) >= .4:
			last = rand
			yield rand
		rand = random.random()
	yield rand

gen = randomwalk_generator()
try:
	while 1: print gen.next().
except StopIteration:
	pass

for num in randomwalk_generator():
	print_short(num)


#recursive generator/ yielding

def inorder(t):
	if t:
		for x in inorder(t.left):
			yield x
		yield t.label
		for x in inorder(t.right):
			yield x

	





















