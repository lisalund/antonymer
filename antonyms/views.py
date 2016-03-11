from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse


def index(request):
	return render(request, 'antonyms/index.html', {})