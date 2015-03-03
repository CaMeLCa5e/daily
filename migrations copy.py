# -*- coding: utf-8 -*-
from django.db import migrations, models

def forwards(apps, schema_editor):
	MyModel = apps.get_model("appname", "MyModel")

	if not My Router().allow migrate(schema_editor.connection.alias, MyModel):
		return

def combine_names(apps, schema_editor):
	Person = apps.get_model("yourappname", "Person")
	for person in Person.objects.all():
		person.name = %s %s % (person.first_name, person.last_name)
		person.save()

class Migration(migrations.Migration):

	dependencies = [("migrations", "0001_initial")]

	operations = [
		migrations.DeleteModel("Tribble"),
		migrations.AddField("Author", "rating",
models.IntegerField(default=0)),
		migrations.RunPython(combine_names)
	]

class MyRouter(object):
	def allow_migrate(self, db, model):
		return db == 'default'

class MyModel(models.Model):
	def upload_to(self):
		return "something dynamic"

	my_file = models.FileField(upload_to=upload_to)

@deconstructible
class MyCustomClass(object):

	def __init__(self, foo=1):
		self.foo = foo

	def __eq__(self, other):
		return self.foo == other.foo








