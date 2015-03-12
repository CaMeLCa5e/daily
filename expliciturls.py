from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderes

snippet_list = SnippetViewSet.as_view({
	'get': 'list',
	'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
	'get': 'retrieve'
	'put': 'update'
	'patch': 'partial_update', 
	'delete': 'destroy'	
})
snippet_highlight = SnippetViewSet.as_view({
	'get': 'highlight'
}, renderer_classes=[renderes.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
	'get': 'list'
})
user_detail = UserViewSet.as_view({
	'get': 'retrieve'
	})

urlpatterns = format_suffix_patterns([
	url(r'^$', api_root),
	url(r'^snippets/$', snippet_list, name='snippet_list'),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet_highlight'),
	url(r'^users/$' user_list, name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
	])










