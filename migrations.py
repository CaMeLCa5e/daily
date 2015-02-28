from django.db import models, migrations
from django.db.migrations.operations.base import Operation

def forwards_func(apps, schema_editor):
	Country = apps.get_model('myapp', 'Country')
	db_alias = schema_editor.connection.alias 
	Country.objects.using(db_alias).bulk_create([
		Country(name="USA", code="us"), 
		Country(name="France", code="fr")
		])

class Migration(migrations.Migration):

	dependencies = []

	operations = [
		migrations.RunPython(
			forwards_func,

		),
	]

class MyCustomOperation(Operation)