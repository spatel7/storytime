from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	return render_to_response('storiesapp/index.html', {}, context)

def login(request):
	context = RequestContext(request)
	return render_to_response('storiesapp/login.html', {}, context)

def register(request):
	context = RequestContext(request)
	return render_to_response('storiesapp/register.html', {}, context)