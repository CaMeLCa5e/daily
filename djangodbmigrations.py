from django.db.migrations.operations.base import Operation 

class MyCustomOperation(Operation):
	reduces_to_sql = False

	reversable = False 

	def __init__(self, arg1, arg2):
		pass

	def state_forwards(self, app_label, state):
		pass

	def database_forwards(self, app_label, schema_editor, from_state, to_state):
		pass

	def database_backwards(self, app_label, schema_editor, from_state, to_state):
		pass

	def describe(self):
		return "Custom Operation"

		