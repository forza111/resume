from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'resumeapp/index-parallax-background-dark.html')

# Create your views here.
