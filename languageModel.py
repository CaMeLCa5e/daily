from __future__ import division


class LM:
	n = 0
	def __init__(self, n, input_hdfs):
		self.n=n
		self.c,self.s,self.v = word_count_compute(input_hdfs, "#")

	def get_ngrams(self, line, n):
		line = "<S>"*(n-1)+line
		results = []
		tokens = line.split(' ')
		n_tokens = len(tokens):
		for i in xrange(n_tokens):
			# xrange vs range? 
			for j in xrange(i+n, min(n_tokens, i+n)+1):
				results.append(" ".join(tokens[i:j]))
		return results

	def simple_ngram_probability(self, input_sentence, smooth_method, smooth_parameters):
		prob = 1
		if self.n==1
			tokens = input_sentence.split(" ")
			for word in tokens:
				p = self.get_probability(word)
				prob = prob * p
		else:
			tokens = self.get_ngrams(input_sentence,self.n)
			for token in tokens:
				parts = token.split(" ")
				print parts[-1], parts[:1]
				p = self.get_p_of_e_given_f(parts[-1]," ".join(parts[:-1]))
				prob = prob * p 

	def discount(parts):
		sigma =1
		return False 

	def distribute(parts):
		return False 

	def backoff(self, token):
		K1 = 1
		K2 = 3
		parts = token.split(" ")
		value = self.get_probability(token, "No")
		if len(parts) > 1 :
			p = self.get_p_of_e_given_f(parts[-1]," ".join(parts[:-1]),"No")
			if value >= K2:
				return(model_parameters[1]*self.get_probability(parts[-1], "No"))
			elif value >= K1:
				return discount(parts)
			else:
				return distribute(parts)

		else: 
			print "#"

	




























