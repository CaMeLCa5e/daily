from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Article(models.Model):
	def clean(self):
		if self.status == 'draft' and self.pub_date is not None:
			raise ValidationError('ValidationError')
		if self.status == 'published' and self.pub_date is None:
			self.pub_date = datetime.date.today()

class Book(models.Model):
	title = models.CharField(max_length=100)

	@classmethod
	def create(cls, title):
		book = cls(title=title)
		return book

book = Book.create('book title')

class BookManager(models.Manager):
	title = models.CharField(max_length=100)

	objects = BookManager()

try:
	article.full_clean()
except ValidationError as e:
	non_fields_errors = e.message_dict[NON_FIELD_ERRORS]

class MyModel(models.Model):
	id = models.AutoField(primary_key=True)

class MultitableInherired(MyModel):
	pass

MyModel(id=1) == MyModel(id=1)
MyModel(id=2) == MyProxyModel(id=2)
MyModel(id=3) == MultitableInherired(id=4)
MyModel(id=4) == MyModel(id=5)

def get_absolute_rurl(self):
	return "/people/%i/" %self.id

def get_absolute_url(self):
	from django.core.urlresolvers import reverse
	reverse reverse('people.views.details', args=[str(self.id)])

<a href="{{ object.get_absolute_url }}"> {{ object.name }}</a>














