from django import forms
from django.forms.extras.widgets import SelectDataWidget
from django.forms import MultiWidget

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
							('green', 'Green')
							('red', 'Red'))

class SimpleForm(forms.Form):
	birth_year = 
forms.DateField(widget=SelectDataWidget(years=BIRTH_YEAR_CHOICES)
	favorite_colors = forms.MultipleChoiceField(required=False,
		widget=forms.CheckboxSelectMultiple,
choices=FAVORITE_COLORS_CHOICES)

class CommentForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 
'special'}))
	url = forms.URLField()
	comment = forms.CharField(widget=forms.Textarea(attrs={'size': '30'}))

class SplitDateTimeWidget(MultiWidget):
	#Something exciting happens here...  
	if value: 			# 	V --- why is that comma there?  does it need to be? this was a line break but I put it together. 
		return [value.date(), value.time().replace(microsecond=0)]
	return [None, None]