from django.conf.urls import url
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hack_O_DjangoREST_Tut')

urlpatterns = [
	url(r'^$', schema_view),
	url(r'^funcsongs/$', views.song_list),
    url(r'^songs/$', views.ListSongs.as_view()),
    url(r'^movies/$', views.ListCreateMovies.as_view()),
    url(r'^movie_year/', views.ListMoviesURLRegexExample.as_view()),
    url('^director/(?P<director>.+)/$', views.ExampleMovieDirectorView.as_view())

]