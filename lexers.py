from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objcts.all())

	class Meta:
		model = User 
		fields = ('id', 'username', 'snippets')


def save(self, *args, **kwargs):
	lexer = get_lexer_by_name(self.language)
	linenos = self.linenos and 'table' or False
	options = self.title and {'title': self.title} or {}
	formatter = HtmlFormatter(style=self.style, linenos=linenos,
								full=True, **options)
	self.highlighted = highlighted(self.code, lexer, formatter)
	super(Snippet, self).save(*args, **kwargs)

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	

