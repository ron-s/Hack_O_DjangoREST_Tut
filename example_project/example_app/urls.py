from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Example_project_api_root, name='root'),
    url(r'^songs/$', views.ListSongs.as_view(), name='song-list'),
]