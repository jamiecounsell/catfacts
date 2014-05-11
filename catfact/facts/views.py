from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.

def home(request):

	return HttpResponse("meow")
