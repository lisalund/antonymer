from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #Adds a decorator for pages that need login. If the user isn't logged in, take them to login page before.
# to make use of login_required: add @login_required above the def-line for view.

def index(request):
	return render(request, 'antonymapp/index.html', {})


def login(request):
	return render(request, 'antonymapp/login.html', {})

@login_required
def play(request):
	return render(request, 'antonymapp/play.html', {})

def highscores(request):
	return render(request, 'antonymapp/highscores.html', {})