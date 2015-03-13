from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.models import Snippet 
from snippets.serializer import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


urlpatterns = [
	url(r'^snippets/$', views.SnippetList.as_view()),
	url(r'^snippets/(?<pk>[0-9]+)/$', views.SnippetDetail.as_view())

	]

	urlpatterns = format_suffix_patterns(urlpatterns)

class SnippetList(mixins.ListModelMixin,
					mixin.CreateModelMixin,
					generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	