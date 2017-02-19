from rest_framework import generics

from . import models
from . import serializers


class ListSongsURLRegexExample(generics.ListAPIView):
    """
    An example of a view that takes a url parameter that is specified in the URL 
    pattern in 'url_params.py'.  
    """

    serializer_class = serializers.SongSerializer

    def get_queryset(self):
        """
        Returns a queryset that is filtered by the song_year argument
        Example of request URL: 'https://example.com/songs/1997' 
        """
        song_year = self.kwargs['song_year']
        return models.Songs.objects.filter(song_year__exact=song_year)


class ListSongsQuerystringExample(generics.ListAPIView):
    serializer_class = serializers.SongSerializer

    def get_queryset(self):
        """
        Returns a queryset filtered by song_year if one present in the 
        URL, else it returns all objects in Songs model. 
        Example of request: 

        'https://example.com/songs/?song_year=1997' --> filters on year 1997
        'https://example.com/songs/' --> returns all songs

        """
        queryset = models.Songs.objects.all()
        song_year = self.request.query_params.get('song_year', None)

        if song_year is not None:
            queryset = queryset.filter(song_year__exact=song_year)
        return queryset






