# ------------------------------------------
# generics class to make writing endpoints easier
from rest_framework import generics
# ------------------------------------------

# ------------------------------------------
# main pieces of DRF that need to be linked
from . import models
from . import serializers
# ------------------------------------------


class ListSongs(generics.ListAPIView):
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer



