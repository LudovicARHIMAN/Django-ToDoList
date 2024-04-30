from django.shortcuts import render
from django.views.generic import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView
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


'''
def home(response):
    return render(response, 'main/home.html')





def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i"  %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form":form})



def View_List(response):
    return render(response, 'main/view.html', {})
'''


# Class Based View
class Index(DetailView):
    model = ToDoList
    template_name = 'main/list.html'
    context_object_name = 'ls'

    def post(self, request, *args, **kwargs):
        ls = self.get_object()

        if ls in request.user.todolist.all():
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif request.POST.get("newItem"):
                txt = request.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("error")

            return render(request, 'main/list.html', {"ls": ls})
        return render(request, 'main/view.html', {"ls": ls})



class Home(View):
    template_name = 'main/create.html'

    def post(self, response):
        return render(response, self.template_name)

class Create(View):
    template_name = 'main/create.html'

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
        return render(response, self.template_name, {"form":form})



class View_List(View):
    template = 'main/view.html'
    
    def get(self, response):
        return render(response, self.template_name, {})