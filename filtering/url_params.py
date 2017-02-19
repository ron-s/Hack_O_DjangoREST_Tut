from django.conf.urls import url
from . import views

urlpatterns = [
    # ---------------------------------------------------------------
    # these are our regular url patterns that don't accept arguments
    url(r'^funcsongs/$', views.song_list),
    url(r'^songs/$', views.ListSongs.as_view()),
    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    # this url pattern will let us grab any characters after the 'songsfilter/'
    # portion of our endpoint and use the 'song_year' variable in our view
    # this endpoint requires something to be present after the 'songsfilter/'
    # protion of the URL
    url('^songsfilter/(?P<song_year>.+)/$', views.ListSongsURLRegexExample.as_view()),
    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    # Example of URL pattern that accepts a query string parameter 
    url(r'^songsquery/', views.ListSongsQuerystringExample.as_view()),
    # ---------------------------------------------------------------
]