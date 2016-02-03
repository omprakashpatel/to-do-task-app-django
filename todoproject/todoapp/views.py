from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("TodoAPP Index")

def post_task(request):
	pass
