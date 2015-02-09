#! usr/bin/python 
#memoizatin to make recursive fibonacci

MemoTable = {}

def MemoizedFib(n):
	if n <= 2:
		return 1

	if n in MemoTable:
		return MemoTable[n]

	MemoTable[n] = MomoizedFib(n-1) + MemoizedFib(n-2)
	return MemoTable[n]

res = MemoizedFib(10)