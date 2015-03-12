from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)

serializer = SnippetSerializer(data=data)
serializer.is_valid()
#True
serializer.validated_data
serializer.save()

class SnipperSerializer(serializer.ModelSerializer):
	class Meta:
		model = Snippet 
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style')