# isvalid
data = {'subject': 'hello',
		'message': 'hi there',
		'sender': 'foo@example.com',
		'cc_myself': True}
f = ContactForm(data)
print f
print f.is_valid()
