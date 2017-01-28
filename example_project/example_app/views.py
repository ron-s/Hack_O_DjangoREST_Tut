from django.shortcuts import render

from rest_framework import generics
from . import models
from . import serializers

class Songs(generics.ListCreateAPIView):
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer


