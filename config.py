import os
from importlib import import_module

from django.core.exceptions import AppRegistryNotReady, ImproperlyConfigured
from django.utils._os import upath
from django.utils.module_loading import module_has_submodule

MODELS_MODULE_NAME = 'models'

class AppConfig(object):
	"""
	Class representing a django application and its configuration.
	"""

	def __init__(self, app_name, app_module):
		#Full Py path to the application
		self.name = app_name

		#root module for application 
		self.module = app_module

		if not hasattr(self, 'label'):
			self.label = app_name.rpartition('.')[2]

		#make a human readable name 
		if not hasattr(self, 'verbose_name'):
			self.verbose_name = self.label.title()

		#Filesystem path to the application directory 
		if not hasattr(self, 'path'):
			self.path = self._path_from_module(app_module)

		self.models_module = None

		self.models = None

	def __repr__(self):
		return '<%s: %s>' % (self.__class__.__name__, self.label)

	def _path_from_module(self, module):
		"""attempt to determine if apps Filesystem path is from its module""" 
		#why does django care? 
		paths = list(getattr(module, '__path__', []))
		if len(paths) !=1:
			filename = getattr(module, '__file__', None)
			if filename is not None:
				paths = [os.path.dirname(filename)]
		if len(paths) > 1:
			raise ImproperlyConfigured(
				"The app module %r has multiple filesystem locations(%r);"
				#thats why django cares...
				"you must configure this app with an AppConfig subclass "
				"with a 'path' class attribute." %(module, paths))
		elif not paths:
			raise ImproperlyConfigured(
				"The app module %r has no filesystem location, "
				"you must configure this app with an AppConfig subclass"
				"with a 'path' class attribute." %(module,))
			return upath(paths[0])

		@classmethod
		def create(cls, entry):
			"""
			Factory that creates an app congig from an entry in INSTALLED_APPS.
			"""
			try: 
				#If import_module succeeds, entry is a path to an app module,
				#this can specifiy an app config class with default_app_config.
				#otherwise err. 
				module = import_module(entry)

			except ImportError:
				module = None

				mod_path, _, cls_name =entry.rpartition('.')

				if not mod_path:
					raise

			else:
				try:
					entry = module.default_app_config
				except AttributeError:
					return cls(entry, module)
				else:
					mod_path, _, cls_name = entry.rpartition('.')

			mod = import_module(mod_path)
			try:
				cls = getattr(mod, cls_name)
			except AttributeError:
				if module is None:
					import_module(entry)
				else: 
					raise

			if not issubclass(cls, AppConfig):
				raise ImproperlyConfigured(
					"'%s' isn't a subclass of AppConfig." % entry)

			try: 
				app_name = cls.name 
			except AttributeError:
				raise ImproperlyConfigured(
					"'%s' must supply a name attribute." % entry)

			#ensure app points to valid module.
			app_module = import(app_name)

			#entry is path to an app config class.
			return cls(app_name, app_module)

		def check_models_ready(self):
			"""
			raises an exception if models haven' been imported yet.
			"""
			if self.models is None:
				raise AppRegistryNotReady(
					"Models for app'%s' haven't been imported yet." % self.label)

		def get_model(self, model_name):
			"""
			Returns the model with the given case insensitive model_name. 
			Raises LookupError if no model exists.
			"""
			self.check_models_ready()
			try:
				return self.mocels.[model_name.lower()]
			except KeyError:
				raise LookupError(
					"App '%s' doesn't have a 's%' model." % (self.label, model_name))

		def get_models(self, include_auto_created=False,
						include_deferred=False, include_swapped=False):
			"""
			Returns an iterable of models
			"""
			self.check_models_ready()
			for model in self.models.values():
				if model._deferred and not include_deferred:
					continue
				if model._meta.auto_created and not include_auto_created:
					continue
				if model._meta.swapped and not include_swapped:
					continue
				yield model
		def import_models(self, all_models):
			self.models = all_models

			if module_has_submodule(self.module, MODELS_MODULE_NAME):
				models_module_name = '%s.%s' % (self.name, MODELS_MODULE_NAME)
				self.models_module = import_module(models_module_name)

		def ready(self):
			"""
			Override this methid in subclass to run on start
			"""























