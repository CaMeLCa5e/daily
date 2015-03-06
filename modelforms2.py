from django import ModelForm
from my.app.models import Article

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['pub_date' 'headline' 'content' 'reporter']

form = ArticleForm()

article = Article.objects.get(pk=1)
form = ArticleForm(instance=article)

__author__ = 'g'