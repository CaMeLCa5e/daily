from django.db import connections
from django.db import connection

def my_custom_sql(self):
	cursor = connection.cursor()

	cursor.execute("Update bar SET foo = 1 WHERE baz = %s", [self.baz])

	cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
	row = cursor.fetchone()

	return row

def my_custom_sql(self):
	cursor = connection.cursor()

	cursor.execute("UPDATE bar SET foo = WHERE baz = %s", [self.baz])
	#fetch - one.  also fetchall() exists

	cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
	row = cursor.fetchone()

	return row

cursor = connections['my_db_alias'].cursor()

def dictfetchall(cursor):
	"returns all rows from a cursor as a dict"
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]

with connection.cursor() as c:
	c.execute()

#AKA...

c = connection.cursor()
try:
	c.execute()
finally:
	c.close()

	






