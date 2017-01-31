from django.shortcuts import render

from rest_framework import generics
import django_filters
from . import models
from . import serializers

class Songs(generics.ListCreateAPIView):
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer

    # still doesn't seem to be working 
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


