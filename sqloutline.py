class Person(models.Model):
	first_name = models.CharField()
	last_name = models.CharField()
	birth_date = models.Datefield()

print [p for p in Person.objects.raw('SELECT * FROM myapp_person')]


for p in Person.objects.raw('SELECT id, first_name FROM myapp_person')
	print(p.first_name,
			p.last_name)

