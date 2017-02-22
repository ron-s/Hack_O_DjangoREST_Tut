from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Songs
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Movies
		fields = '__all__'