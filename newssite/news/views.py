from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! You are currently visiting this news site that is currently a WIP.")
