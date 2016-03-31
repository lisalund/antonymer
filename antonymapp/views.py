from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required  #Adds a decorator for pages that need login. If the user isn't logged in, take them to login page before.
# to make use of login_required: add @login_required above the def-line for view.
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import SomeForm
from django.template import RequestContext

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
@csrf_protect
def play(request):
    if request.method == 'POST':
        form = SomeForm(request.POST)
        print form.is_valid() 
        if form.is_valid():
            picked = form.cleaned_data.get('picked')
            # do something with your results
            picked = int(picked[0])
            player = request.user.userprofile
            player.score = player.score + picked
            player.save()
    else:
        form = SomeForm

    return render(request, 'antonymapp/play.html', {'form':form })