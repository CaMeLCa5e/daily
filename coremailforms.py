# coremailforms.py

<p><label for="id_subject>Subject:</label>"
	<input id="id_subject" type="text" name="subject" maxlength="100"/>
</p>
<p><label for="id_message">Message:</label>
	<input type="text" name="message" id="id_message" /></p>
<p><label for "id_sender">Sender:</label>
	<input type="email" name="sender" id="id_sender" /><p>
<p><label for="id_cc_myself">CC Myself:</label>
	<input type="checkbox"> name="cc_myself" id="id_cc_myself" /></p>

# {{ form.as_table}}  Renders cells wrapped in <tr>
# {{ form.as_p}} Renders cells wrapped in <p>
# {{ form.as_ul}} Renders cells wrapped in <li>

{{ form.non_field_errors }}
<div class="fieldWrapper">
	{{ form.subject.errors }}
	<label for="{{ form.subject.id_for_label }}">Email subject:</label>
	{{ form.subject }}
</div>
<div class="fieldWrapper">
	{{ form.message.errors }}
	<label for-"{{ form.message.id_for_label }}">Your message:</label>
	{{ form.message }}
</div>
<div class="fieldWrapper">
	{{ form.sender.errors }}
	<label for="{{ form.sender.id_for_label }}">Your email address:
</label>
	{{ form.sender }}
</div class="fieldWrapper">
	{{ form.cc_myself.errors }}
	<label for="{{ form.cc_myself.id_for_label }}">CC yourself?</label>
	{{ form.cc_myself }}
</div>

<div class="fieldWrapper">
	{{ form.subject.errors }}
	{{ form.subject.label_tag}}
	{{ form.subject }}
</div>

<ul class="errorlist">
	<li>Sender is required.</li>
</ul>



























