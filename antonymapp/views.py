from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #Adds a decorator for pages that need login. If the user isn't logged in, take them to login page before.
# to make use of login_required: add @login_required above the def-line for view.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
	return render(request, 'antonymapp/index.html', {})


def login(request):
	return render(request, 'antonymapp/login.html', {})

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            new_user = User.objects.create_user(username=username, password=password)
            return redirect('play')
    else:
        form = UserCreationForm()

    return render(request, 'antonymapp/create_user.html', {'form': form}) 

@login_required
def play(request):
	return render(request, 'antonymapp/play.html', {})

def highscores(request):
	return render(request, 'antonymapp/highscores.html', {})