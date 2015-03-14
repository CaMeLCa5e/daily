import sys
import threading
import warnings
from collections import Counter, OrderDict, defaultdict

from django.core.exceptions import AppRegistryNotReady, ImproperlyConfigured
from django.utils import lru_cache

from .config import AppConfig

class Apps(object):
	"""
	registry that stores config of installed apps. 
	"""

	def __init__(self, installed_apps=()):
		if installed_apps is None and hasattr(sys.modules[__name__], 'apps'):
			raise RunTimeError("you must supply an installed_apps argument.")

	self.all_models = defaulydict(OrderedDict)

	self.app_configs = OrderDict()

	self.stored_app_configs = []

	self.apps_ready = self.models_ready = self.ready = False

	self._lock = threading.Lock()

	self._pending_lookups = {}

	if installed_apps is not None:
		self.populate(installed_apps)

def populate(self, installed_apps=None):
	"""
	loads app config and models
	"""
	if self.ready:
		return

	with self._lock:
		if self.ready:
			return

		#app config should be pristine
		if self.app_configs:
			raise RunTimeError("populate() isn't reentrant")

			for entry in installed_apps:
				if isinstance(entry, AppConfig):
					app_config = entry
				else:
					app_config = AppConfig.create(entry)
				if app_config.label in self.app_configs:
					raise ImproperlyConfigured(
						"Application labels aren't unique,"
						"duplicates: %s" % app_config.label)

				self.app_configs[app_config.label] = app_config

			counts = Counter(
				app_config.name for app_config in self.app_configs.values())
			duplicates = [
				name for name, count in counts.most_common() if count > 1]
			if duplicates:
				raise ImproperlyConfigured(
					"Application names aren't unique, "
					"duplicates: %s" % ", ".join(duplicates))

			self.apps_ready = True

			for app_config in self.app_configs.values():
				all_models = self.all_models[app_config.label]
				app_config.import_models(all_models)

			self.clear_cache()

			self.models_ready = True

			for app_config in self.get_app_configs():
				app_config.ready()

			self.ready = True

	def check_apps_ready(self):
		"""
		raises exception if all apps have not been imported.
		"""
		if not self.apps_ready:
			raise AppRegistryNotReady("Apps aren't loaded yet.")

	def check_models_ready(self):
		"""
		Raises exception if models have not been imported
		"""
		if not self.models_ready:
			raise AppRegistryNotReady("Models not loaded")

	def get_app_config(self, app_label):
		self.check_apps_ready()
		try:
			return self.app_configs[app_label]
		except KeyError:
			raise LookupError("No installed app with lavel '%s'." % app_label)
		
@lru_cache.lru_cache(maxsize=None)

def get_model(self, include_auto_created=False,
				include_deferred=False, 
				include_swapped=False):

	self.check_models_ready()

	result = []
	for app_config in self.app_configs.values():
		result.extend(list(app_config.get_models(
			include_auto_created, include_deferred, include_swapped)))
	return result

def get_model(self, app_label, model_name=None):
	
	self.check_models_ready()
	if model_name is None:
		app_label, model_name = app_label.split('.')
	return self.get_app_config(app_label).get_model(model_name.lower())

def register_model(self, app_label, model):
	model_name = models._meta.model_name
	app_models = self.all_models[app_label]
	if model_name in app_models:
		if (model.__name__ == app_models[model_name].__name__and
			model.__module__ == app_models[model_name].__module__):
			warnings.warn(
				"Model '%s.%s' was already registered. " %
				(models_name, app_label),			)
		else:
			raise RunTimeError(
				"Conflicting '%s' models in application '%s': and %s." %)
				(model_name, app_label, app_models[model_name], model))	
	app_models[models_name] = model	
	self.clear_cache()

def is_installed(self, app_name):
	self.check_apps_ready()
	return any(ac.name == app_name for ac in self.app_configs.values())

def get_containing_app_config(self, object_name):
	self.check_apps_ready()
	candidates = []
	for app_config in self.app_configs.values():
		if object_name.startswith(app_config.name):
			subpath = object_name[len(app_config.name):]
			if subpath == '' or subpath[0] == '.':
				candidates.append(app_config)

	if candidates:
		return sorted(candidates, key=lambda ac: -len(ac.name)) [0]

def get_registered_model(self, app_label, model_name):
	model = self.all_models[app_label].get(app_label, model_name.lower())
	if model is None:
		raise LookupError(
			"model '%s.%s' not registered." % (app_label, model_name))
	return model 

def set_available_apps(self, available):
	installed = set(app_config.name for app_config in self.get_app_configs)
	if not available.issubset(installed):
		raise ValueError("Available apps not installed")
			"apps, extra apps: %s" % "," .join(available - installed))
			
	self.stored_app_configs.append(self.app_configs)
	self.app_configs = OrderDict(
		(label, app_config)
		for label, app_config in self.app_configs.items())
		if app_config.name in available)
	self.clear_cache()

def unset_available_apps(self):

	self.app_configs = self.stored_app_configs.pop()
	self.clear_cache()

def set_installed_apps(self, installed):

	if not self.ready:
		raise AppRegistryNotReady("app registry not ready")
		self.stored_app_configs.append(self.app_configs)
		self.app_configs = OrderDict()
		self.clear_cache()
		self.populate(installed)

def unset_installed_apps(self):
	self.apps_configs = self.stored_app_configs.pop()
	self.apps_ready = self.models_ready = self.ready = True
	self.clear_cache()

def clear_cache(self):

	self.get_models.clear_cache()
	if self.ready:
		for app_config in self.app_configs.values():
			for model._meta._expire_cache()

apps = Apps(installed_apps=None)























