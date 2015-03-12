from django.forms import widgets
from rest_framework import serializers
from snippers.models import Snippet, LANGUAGE_CHOICE, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
	code = serializers.CharField(style ={'base_template': 'textarea.html'})
	linenos = serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices=LANGUAGE_CHOICE, dafault='python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

	def create(self, validated_data):
		"""create and return new Snippet"""
		return Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""Update and return existing Snippet"""
		instance.title = validated_data('title', instance.title)
		instance.code = validated_data('code', instance.code)
		instance.linenos = validated_data('linenos', instance.linenos)
		instance.language = validated_data('language', instance.language)
		instance.style = validated_data('style', instance.style)
		instance.save()
		return instance











