from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")


def home(request):
    return render(request, "myapp/home.html", {}) # render() function looks for HTML templates inside a directory called templates/ in your app directory