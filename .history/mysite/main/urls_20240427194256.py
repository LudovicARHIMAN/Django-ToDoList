from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("",views.Home.as_view(), name="Home"),
    path("create/",views.Create(), name="Create"),
    path("view/",views.View_List.as_view(), name="View_List"),
]