# ------------------------------------------
# imports needed for the functional view 
from rest_framework.decorators import api_view
from rest_framework.response import Response
# ------------------------------------------

# ------------------------------------------
# generics class to make writing endpoints easier
from rest_framework import generics
# ------------------------------------------

# ------------------------------------------
# main pieces from our DRF app that need to be linked
from . import models
from . import serializers
# ------------------------------------------


@api_view(['GET'])
def song_list(request):
    """
    A function based view that use the api_view decorator to add functionality
    to the view.   
    """
    if request.method == 'GET':
        songs = models.Songs.objects.all()
        serializer = serializers.SongSerializer(songs, many=True)
        return Response(serializer.data)


class ListSongs(generics.ListAPIView):
    """
    A class based view that inherits from the generics class. The generics
    class gives you a convinient way to declare views quickly when you only
    need basic functionality or simple CRUD operations. 
    """
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer


class ListCreateMovies(generics.ListCreateAPIView):
    """
    A class based view that inherits from the movies class
    """
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MovieSerializer










