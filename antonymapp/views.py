from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required  #Adds a decorator for pages that need login. If the user isn't logged in, take them to login page before.
# to make use of login_required: add @login_required above the def-line for view.
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile, WordPair
from .forms import SomeForm
from django.template import RequestContext


rand_list = [17, 41, 47, 27, 5, 38, 19, 31, 33, 37, 26, 42, 30, 18, 44, 35, 32, 28, 39, 34, 46, 6, 9, 45, 40, 50, 11, 36, 25, 21, 29, 8, 49, 12, 10, 3, 13, 48, 7, 20, 23, 2, 15, 16, 1, 4, 22, 43, 24, 14]

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
            #return redirect('play')
    else:
        form = UserCreationForm()

    return render(request, 'antonymapp/create_user.html', {'form': form}) 

# Helper function to play
def update_word_data(argument, word_pair):
    if argument==1:
        word_pair.ones = word_pair.ones + 1
    if argument==2:
        word_pair.two = word_pair.ones + 1
    if argument==3:
        word_pair.three = word_pair.ones + 1
    if argument==4:
        word_pair.four = word_pair.ones + 1
    if argument==5:
        word_pair.five = word_pair.ones + 1
    word_pair.save()

@login_required
@csrf_protect
def play(request):
    user_index = request.user.userprofile.word_index
    if user_index >= 51 :
         return render(request, 'antonymapp/victory.html', {})

    word_index = rand_list[user_index-1]
    word_pair = WordPair.objects.get(id=word_index)
 
    if request.method == 'POST':
        form = SomeForm(request.POST)
        if form.is_valid():
            picked = form.cleaned_data.get('svar')
            # This is where I do things with my result
            picked = int(picked[0])
            player = request.user.userprofile
            consensus = word_pair.calc_mean()
            score = 4 - abs(picked-consensus)
            player.score = player.score + score
            player.word_index = user_index + 1
            player.save()
            update_word_data(picked, word_pair)
            #Now I'm done with my result and want to present a new question to the user
            return redirect('play')
    else:
        form = SomeForm
    return render(request, 'antonymapp/play.html', {'form':form, 'word_pair':word_pair })
