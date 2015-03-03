from django.db import models
from django.conf.urls import url

@models.permalink
def get_absolute_url(self):
	return('people.views.details', [str(self.id)])

@models.permalink
def get_absolute_url(self):
	return ('archive_view', (), {
		'year': self.created.year,
		'month': self.created.strftime('%m'),
		'day': self.created.strftime('%d')})

url(r'^people/(\d+)/$', 'blog_views.generic_detail', name='people_view'),

@models.permalink
def get_absolute_url(self):
	return ('people_view', [str(self.id)])


class Person(models.Model):
	SHIRT_SIZES = (
		(u'S', u'Small'),
		(u'M', u'Medium'),
		(u'L', u'Large'),
		)
	name = models.CharField(max_length=60)
	shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)


