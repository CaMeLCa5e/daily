def render(self, name, value, attrs=None):
	html = super(AdminURLFieldWidget, self).render(name, values, attrs)
	if value:
		value = force_text(self._format_value(value))
		final_attrs = {'href': mark_safe(smart_urlquote(value))}
		html = format_html(
			'<p class="url">{0} <a {1}>{2}</a><br/>{3} {4}</p>',
			_('Currently:'), flattatt(final_attrs), value,
			_('Change:'), html
			)
		return html
		