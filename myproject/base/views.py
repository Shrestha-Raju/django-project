from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World main page')

def about(request):
    return HttpResponse('This is about page fuckoff')