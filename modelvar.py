from django.forms import ModelForm, Textarea
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _ 
from myapp.models import Author
from myapp.models import Article 

class ArticleForm(ModelForm):
	class Meta:
		error_messages = {
			NON_FIELD_ERRORS: {
			'unique_together': "%(model_name)s's %(field_label)s are not unique."
			}
		}

class AuthorFormVar(ModelForm):
	model = Author
	fields = '__all__'

class ParticularAuthorForm(ModelForm):
	class Meta:
		model = Author
		exclude = ['title']

class AuthorFormTextOver(ModelForm):
	class Meta:
		model = Author
		fields = ('name', 'title', 'birth_date')
		widgets = {
			'name': Textarea(attrs={'cols':80, 'rows': 20}),
		}

class AuthorFormGetLazy(ModelForm):
	class Meta:
		model = Author
		fields = ('name', 'title', 'birth_date')
		labels = {
			'name': _('Writer'),
		}
		help_texts = {
			'name': _('Pop and lock it.  Did you see that under... __ #_')
		}
		error_messages = {
			'name': {
				'max_length': _("This writer's name is too long."),
			}
		}
class ArticleFormSlug(ModelForm):
	slug = MySlugFormField()

	class Meta:
		model = Article
		fields = ['pub_date', 'headline', 'content', 'reporter', 'slug']

class BaseAuthorFormSet(BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		super(BaseAuthorFormSet, self).__init__(*args, **kwargs)
		self.quweyset = Author.objects.filter(name__startswith='0')


def manage_authors(request):
	AuthorFormSet = modelformset_factory(Author)
	if request.method == 'POST':
		formset = AuthorFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()

	else:
		formset = AuthorFormSet()
	return render_response("manage_authors.html"),{
		"formset": formset,
	}
	






