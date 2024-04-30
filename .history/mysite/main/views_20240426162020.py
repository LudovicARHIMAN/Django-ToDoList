from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.views import View

# Function Based View

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():
    
        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    
                    item.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("error")
        
        return render(response, 'main/list.html', {"ls":ls})
    return render(response, 'main/view.html', {"ls":ls})



def home(response):
    return render(response, )

class home:
    template = 'main/home.html'
    def get(self, response):
        return render(response, self.template {})




# Class Based View
class create(View):
    template = 'main/create.html'

    def post(self, response):
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i"  %t.id)
    
    def get(self, response):
        form = CreateNewList()
        return render(response, self.template, {"form":form})



class view(View):
    template = 'main/view.html'
    
    def get(self, response):
        return render(response, self.template, {})