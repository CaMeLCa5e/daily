from django import forms

class Calendar Widget(forms.TextInput):
	class Media:
		css = {
			'all': ('pretty.css',)
		}
		js = ('animations.js', 'actions.js')

class Media:
	css = {
		'screen':('pretty.css',),
		'print': ('newspaper.css',)
		'tv, projector':('lo_res.css'),	
	}

class FancyCanendarWidger(CalendarWidget):
	class Media:
		extend = False
		css = {
			'all': ('fancy.css',)
		}
		js = ('whizbang.js')

w = FancyCanendarWidger()
print(w.media)



class CalendarWidget(forms.TextInput):
	def _media(self):
		return forms.Media(css={'all': ('pretty.css',)},
							js=('animations.js', 'actions.js'))
	media = property(_media)