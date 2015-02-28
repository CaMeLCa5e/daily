from django.db import transaction

@transaction.atomic
def viewfunc(request):

	a.save()
	#now conains a save

	sid = transaction.savepoint()

	b.save()

	if want_to_keep_b:
		transaction.savepoint_commit(sid)

@transaction.rollback
def viewfunc(request):
	
	else:
		transaction.savepoint_rollback(sid)

	a.save()
	try:
		b.save
	except IntegrityError, e:
		raise transaction.rollback()
	c.save()


transaction.set_autocommit(False)
try:
	#stuff
finally:
	transaction.set_autocommit()

#Autocommit.  wut? 
with transaction.autocommit():
	try:
		#run process

transaction.set_autocommit(True)
try:
	#this
finally:
	transaction.set_autocommit(False)
	#turn it off. 





















