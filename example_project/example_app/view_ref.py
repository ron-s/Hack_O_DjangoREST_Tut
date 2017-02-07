"""
Use this file as a reference for the different ways to setup generic views 

Docs for generic views: 
http://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
"""

# importing generic functionality from DRf
from rest_framework import generics

# all views need access to the apps models and serializers 
from . import models
from . import serializers

# -------------------------------------------------------------------------
# Simple example of generic view 
# -------------------------------------------------------------------------
class ListCreateSongs(generics.ListCreateAPIView):
    """
    This view below will automatically create a view that gives you built in 
    post and get method handlers. The generics module contatins a bunch of out 
    of the box functionality that you normally need from endpoints. 
    """

    # Each generic view at a minimun needs a queryset and a serializer defined 
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer

    # notice how you don't need a return statement if using generics as is 


# -------------------------------------------------------------------------
# example of filtering on query string parameter in generic view 
# -------------------------------------------------------------------------
class ListSongs(generics.ListAPIView):
    """
    This is an example that only allows GET requests and has an optional 
    query string parameter of 'artist'. If the API user passes in a URL like:
    'https://exampleAPI.com/?artist=test' the view will take the value of artist
    in the query string and turn it into the artist variable below and then 
    make a sub queryset made up of records of songs only from that artist      
    """
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer

    # each request has a .query_params.get() method, using this allows you 
    # to access the the named query parametes using the syntax below
    artist = self.request.query_params.get('artist', None)

    if artist is not None:
        # take the original queryset that contains all rows from Songs and filter 
        # on the 'artist_name' column using regex to pull out only the records that
        # match the artist name in the query string. 

        # !! for PostgreSQL regex must use postgres terms. Here that means 
        # the regex expression should be r'\y{}\y'
        queryset = queryset.filter(artist_name__regex=r"\b{}\b".format(artist))

    return queryset


# -------------------------------------------------------------------------
# example of different ways to filter querysets 
# -------------------------------------------------------------------------
class TrimSongs(generics.ListAPIView):
    """
    This view is only an example of the different methods availible to filter 
    songs and some added browsable functionality availible. If you were to plug 
    all the filters into a view you would most likely get an empty list as a result. 
    """

    # giving the view that basic building blocks it needs to work 
    queryset = models.Songs.objects.all()
    serializer_class = serializers.SongSerializer

    # adds a filter backend that was declared in settings.py 
    # this gives you different ways to filter the response of the view in the browser
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    # example of filter in pseudo code
    filtered_queryset = queryset.filter(columnName__)











