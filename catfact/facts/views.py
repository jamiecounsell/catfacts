from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.

def home(request):
	newCat = None
	context = {}
	return render_to_response('facts/home.html', context)

def signup(request):
	wat = 1