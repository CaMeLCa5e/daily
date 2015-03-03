from lettuce import step
from school.models import Student

# @step('I have the following students in my database:')
# def students_in_database(step):
# 	for student_dict in step.hashes:
# 		person = Student(**student_dict)
# 		person.save

#######

# @step('I have the following students in my database:')
# def students_in_database(step):
# 	person1 = Student(**step.hashes.first)
# 	person2 = Student(**step.hashes.last)

# 	person1.save()
# 	person2.save()

###### AKA...

@step('I have the following students in my database:')
def students_in_database(step):
	assert step.hashes == [
		{
			'name': 'Anton',
			'monthly_due': '$500'
			'billed': 'no'
		},
		{
			'name': 'Jack', 
			'monthly_due': '$0'
			'billed': 'no'
		},
		{
			'name': 'Gloria', 
			'monthly_due': '$800'
			'billed': 'yes'
		}
]

