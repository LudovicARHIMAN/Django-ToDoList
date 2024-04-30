from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import login ,authenticate
from django.contrib.auth.forms import UserCreationForm


def register(response):
    if response.method == "POST":
        
    form = UserCreationForm()
    return render(response, "register/register.html", {"form" : form})