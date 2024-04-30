from django.urls import path, HttpResponse
from . import views

def register(responder):
    return HttpResponse("Hello World" )