from django.urls import path 
from django.http import HttpResponse
from . import views

def register(response):
    return HttpResponse("<h1>Test</h1>")