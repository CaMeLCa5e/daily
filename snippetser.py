#from snippets.serializers import SnippetSerializer
#from django.http importHttpResponse
from django.views.decorators.csrf import csrf_sxempt
from rest_framework.renderers import JSONRenderer
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.conf.urls import url 
from snippets import views



SnippetSerializer():
	id = IntegerField(label='ID', read_only=True)
	title = CharField(allow_blank=True, max_length=100, required=False)
	code = CharField(style={'base_template': 'textarea.html'})
	linenos = BooleanField(required=False)
	language = ChoiceField(choices=[('python', 'python')])
	style = ChoiceField(choices=[('autumn', 'autumn')])

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# def snippet_list(request):
# 	"""list all code snippets or create a new snippet"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializers = SnippetSerializer(snippets, many=True)
# 		return JSONResponse(serializer.data)

# 	elif request.method == 'POST':
# 		data = JSONParser.parse(request)
# 		serializer = SnippetSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data, status=201)
# 		return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
	"""retrieve or delete code snippet"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT'
		data = JSONParser().parse(request)
		serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)

urlpatterns = [
	url(r'^snippets/$', views.snippet_list),]
	url(r'^snippets/(?<pk>[0-9]+)/$', views.snippet_detail),
]




























