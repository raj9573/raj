from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def  rajasekhar(request):
    return HttpResponse('<marquee><h1>Welcome to our website</h1></marquee>')
def harika(request):
    return HttpResponse('<marquee><h1>hai this is the Harika website</h1></marquee>')

