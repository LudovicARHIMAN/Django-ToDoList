from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("",views.Home.as_view(), name="home"),
    path("create/",views.Create.as_view(), name="create"),
    path("view/",views.View_List.as_view(), name="view"),
]