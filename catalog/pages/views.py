from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Hello from pages app</h1>')
    return render(request, "templates/index.html")

def about(request):
    # return HttpResponse('<h1>Hello from pages app</h1>')
    return render(request, "templates/about.html")