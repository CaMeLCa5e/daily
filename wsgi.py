import django
from django.core.handlers.wsgi import WSGIHandler

def get_wsgi_application():

	django.setup()
	return WSGIHandler()
	