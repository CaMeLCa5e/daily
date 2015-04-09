from __future__ import division 
import numpy as np 
from pyspark import SparkContext 

def ngram(line):
	MIN_N = 1
	MAX_N = 4
	results = []
	tokens = line.split(' ')
	n_tokens = len(tokens)
	for i in xrange(n_tokens):
		for j in xrange(i+MIN_N, min(n_tokens, i+MAX_N)+1):
			results.append((" ".join(tokens[i:j]),1))
	return results

def unigram(phrase):
	if len(phrase[0].split(' '))>1:
		return False
	else: 
		return True 
