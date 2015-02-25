# form.py
{%include "form_snippet.html" %}

# In form_snippet.html:
{% for field in form %}
	<div class="fieldWrapper">
		{{ field.errors }}
		{{ field.label_tag }} {{ field }}
	</div>
{% endfor %}

{% include"form_snippet.html" with form=comment_form %}

