from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^funcsongs/$', views.song_list),
    url(r'^songs/$', views.ListSongs.as_view()),
    url(r'^movies/$', views.ListCreateMovies.as_view()),
]