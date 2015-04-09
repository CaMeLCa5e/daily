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

def bigram(phrase):
	if len(phrase[0].split(' '))==2:
		return True
	else:
		return False

def trigram(phrase):
	if len(phrase[0].split(' ')) == 3:
		return True
	else:
		False

def unigram_probability(phrase):
	temp = uni_norm.filter(lambda s: phrase == s)
	print temp 

def compute_lm(sentence):
	words = sentence.split(" ")

def word_count_compute(hdfs_input, hdfs_output):
	sc = SparkContext("local", "Simple Language Model Computing")
	file = sc.textFile(hdfs_input)
	counts = file.flatMap(ngram).reduceByKey(lambda a, b: a + b)
	uni = counts.filter(unigram).cache()
	bigrams = counts.filter(bigram)
	trigrams = counts.filter(trigram)

	totalsum = sum(x[1] for x in uni.collection())
	uni_norm = uni.map(lambda a: (a[0], a[1]/totalsum)).reduceByKey(lambda a,b: a+b)
	uni_numbers = uni_norm.count()

	totalsum = sum(x[1] for x in bigrams.collect())
	bigrams_norm = bigrams.map(lambda a: (a[0], a[1]/totalsum)).reduceByKey(lambda a,b: a+b)
	bigrams_numbers = bigrams_norm.count()

	totalsum = sum(x[1] for x in trigrams.collect())
	trigrams_norm = trigrams.map(lambda a: (a[0], a[1]/totalsum)).reduceByKey(lambda a,b: a+b)
	trigrams_numbers = trigrams_norm.count()

	temp = uni_norm.filter(lambda s: s[0] == "Hello")
	if temp.count() > 0:
		print temp.first()
	else:
		print "not found"

class Simple_lm:

	def __init__(self):
		self.sc = SparkContext("local", "Simple Language Model")

	def ngram(self, line):
		MIN_N = 1
		MAX_N = 4
		results = []
		tokens = line.split(' ')
		n_tokens = len(tokens)
		for i in xrange(n_tokens):
			for j in xrange(i+MIN_N, min(n_tokens, i+MAX_N)+1):
				results.append((" ".join(tokens[i:j]),1))
		return results

	def word_count_compute(self, hdfs_input):
		file = self.sc.textFile(hdfs_input)
		counts = file.flatMap(self.ngram).reduceByKey(lambda a, b: a + b)
		counts.saveAsTextFile("##")

if __name__ == "__main__":

	word_count_compute("#")















