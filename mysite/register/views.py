from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import login ,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Function Based Views
'''
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        redirect("/home")
    else:
        form = RegisterForm()
    
    return render(response, "register/register.html", {"form" : form})
'''

#class based views
class Register(View):
    template_name = "register/register.html"

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        
        redirect("/home")


    def get(self,request):
        form = RegisterForm()
        context = {
            "form" : form
        }

        return render(request, self.template_name, context)
        