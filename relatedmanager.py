from django.db import models

class Reporter(models.Model):
	pass

class Article(models.Model):
	reporter = models.ForeignKey(Reporter)

class Topping(models.Model):
	pass

class pizza(object):
	"""docstring for pizza"""
	def __init__(self, arg):
		super(pizza, self).__init__()
		self.arg = arg
		