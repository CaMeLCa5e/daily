f = ContactForm()

data = {'subject'; 'hello',
		'message': 'Hi there',
		'sender': 'foo@example.com',
		'cc_myself': True}
f = ContactForm(data)
print f.is_bound

f = ContactForm({'subject': 'hello'})
print f.is_bound