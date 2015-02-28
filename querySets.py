from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)

class DahlBookManager(models.Model):
	def get_queryset(self):
		return super(DahlBookManager, 
self).get_queryset().filter(author='Roald Dahl')

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)

	objects = models.Manager()
	dahl_objects = DahlBookManager()

Book.dahl_objects.all()
Book.dahl_objects.filter(title='Matilda')
Book.dahl_objects.count()

class AuthorManager(models.Manager):
	def get_queryset(self):
		return super(AuthorManager, self).get_queryset().filter(role='A')

class EditorManager(models.Manager):
	def get_queryset(self):
		return super(EditorManager, self).get_queryset().filter(role='E')

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	role = models.CharField(max_length=1, choices=(('A', _('Author')),
('E', _('Editor'))))
	people = models.Manager()
	authors = Author.Manager()
	editors = Editor.Manager()
