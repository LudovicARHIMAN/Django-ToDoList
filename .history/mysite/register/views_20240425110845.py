from django.urls import path 
from django.http import HttpResponse
from . import views

def register(response):
    return HttpResponse("Test )