from django.shortcuts import render
from django.http import HttpResponse

def view(request):
    return HttpResponse('<marquee> <h1>This is main Heading</h1> </marquee>')

# Create your views here.
