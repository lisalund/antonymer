    url(r'^$', views.index, name = 'index'),
    url(r'^login', views.login, name='login'),
    url(r'^play', views.play, name='play'),
    url(r'^highscores', views.highscores, name='highscores'),