from django.db import transaction
from django.db import IntegrityError, transaction


@transaction.non_atomic_requests
def my_view(request):
	do_stuff()

@transaction.non_atomic_requests(using='other')
def my_other_view(request):
	do_stuff_on_the_other_database()

@transaction.non_atomic_requests
def viewfun(request):
	do_stuff()

	with transaction.atomic()
	do_more_stuff()

@transaction.atomic
def viewfun(request):
	create_parent()

	try:
		with transaction.atomic()
			generate_relationships
	except IntegrityError:
		handle_exception()

	add_children()

@transaction.atomic
def viewfun(request):
	a.save()

	sid = transaction.savepoint()

	b.save()

	if want_to_keep_b:
		transaction.savepoint_commit(sid)

	else:
		transaction.savepoint_rollback(sid)


a.save()
sid = transaction.savepoint()
try:
	b.save()
	transaction.savepoint_commit(sid)
except IntegrityError:
	transaction.savepoint_rollback(sid)
c.save()














