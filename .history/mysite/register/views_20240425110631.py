from django.urls import path, HttpResponse
from . import views

def register(responder):
    return HttpResponse("<h1>%s</h1> <br></br> <p>%s</p>" 