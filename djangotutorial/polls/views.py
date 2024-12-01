from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Myhtml(request):
    return HttpResponse("<h1>Testing view to understand the url and view system in both polls and mysite</h1>")
