from rest_framework import viewsets
from rest_framework.decorators import detail_route

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Viewset provides list and detail action
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	provides list, create, retrieve, update and destroy
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly,)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, seriallizer):
		seriallizer.slave(owner=self.request.user)

		
