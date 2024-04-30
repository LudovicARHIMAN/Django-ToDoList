from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.views.generic import View, TemplateView, ListView

from .api.serializers import ToDoListSerializers


from rest_framework.views import APIView
from rest_framework.response import Response



# Function Based Views
'''
def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if ls in request.user.todolist.all():
    
        if request.method == "POST":
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
        
        return render(request, 'main/list.html', {"ls":ls})
    return render(request, 'main/view.html', {"ls":ls})



def home(request):
    return render(request, 'main/home.html')


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i"  %t.id)
    else:
        form = CreateNewList()
    return render(request, 'main/create.html', {"form":form})



def View_List(request):
    return render(request, 'main/view.html', {})
'''

# Class Based Views
class Index(View):
    template_name_list = 'main/list.html'
    template_name_view = 'main/view.html'

    def get(self, request, id):
        ls = ToDoList.objects.get(id=id)
        context = {
            "ls" : ls
        }

        if ls in request.user.todolist.all():
            return render(request, self.template_name_list, context)
        
        return render(request, self.template_name_view, context)

    def post(self, request, id):
        ls = ToDoList.objects.get(id=id)
        context = {
            "ls" : ls
        }

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

            return render(request, self.template_name_list, context)

        return render(request, self.template_name_view, context)



class Home(TemplateView):
    template_name = 'main/home.html'


class Create(View):
    template_name = 'main/create.html'

    def post(self, request):
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
            return HttpResponseRedirect("/%i" % t.id)

    def get(self, request):
        form = CreateNewList()
        context = {
            "form" : form
        }
        return render(request, self.template_name, context)


class View_List(TemplateView):
    template_name = 'main/view.html'


# API Class Views 
class ToDoListView(APIView):
    '''
    Créer des Listes via l'API
    '''
    
    def get(self, request):
            queryset = ToDoList.objects.all()
            serializer = ToDoListSerializers(queryset, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = ToDoListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
