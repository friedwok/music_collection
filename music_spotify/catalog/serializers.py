from rest_framework import serializers

from .models import Genre

class GenreSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return Article.objects.create(**validated_data)
