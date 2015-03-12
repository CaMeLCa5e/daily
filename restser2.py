from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parser import JSONParser

snippet = Snipper(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "Hello Rest"\n')

snippet.save()

