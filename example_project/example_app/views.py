# ------------------------------------------
# imports needed for root endpoint
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
# ------------------------------------------

# ------------------------------------------
# generics class to make writing endpoints easier
from rest_framework import generics
# ------------------------------------------

# ------------------------------------------
# main pieces of DRF that need to be linked
from . import models
from . import serializers
# ------------------------------------------


@api_view(['GET'])
def Example_project_api_root(request, format=None):
    "The following endpoints are available"
    return Response({
        'Songs list': 
        reverse('example_app:song-list', request=request, format=format),       

    })

class ListSongs(generics.ListCreateAPIView):
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer



