from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^play', views.play, name='play'),
    url(r'^highscores', views.highscores, name='highscores'),
    url(r'^create_user/$', views.create_user, name='create_user'),
]