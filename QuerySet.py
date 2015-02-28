class PersonQuerySet(models.PersonQuerySet):
	def authors(self):
		return self.filter(role='A')

	def editors(self):
		return self.filter(role='E')

class PersonManager(models.Manager):
	def get_queryset(self):
		return PersonQuerySet(self.model, using=self._db)

	def authors(self):
		return self.get_queryset().authors()

	def editors(self):
		return self.get_queryset().editors()

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	role = models.CharField(max_length=1, choices=(('A', _('Author')),
('E'_('Editor'))))
	people = PersonManager()

class CustomQuerySet(models.QuerySet):
	def public_method(self):
		return

	def _private_method(self):
		return
	def opted_out_public_method(self):
		return
	opted_out_public_method.queryset_only = False

class MyModel(models.Model):
	objects = CutstomManager()

class AbstractBase(models.Model):
	objects = CutstomManager()

	class Meta:
		abstract = True

class ChildA(AbstractBase):
	pass

class ExtraManager(models.Model):
	extra_manager = OtherManager()

	class Meta:
		abstract = True

class ChildC(AbstractBase, ExtraManager):
	pass

















