@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
	"""
	Retrieve update or delete
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippt)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

		





