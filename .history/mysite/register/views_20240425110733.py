from django.urls import path, HttpResponse
from . import views

def register(response):
    return HttpResponse("Test" )