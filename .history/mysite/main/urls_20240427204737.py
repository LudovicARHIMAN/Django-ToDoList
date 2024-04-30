from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.Index.as_view(), name="index"),
    path("",views.Home.as_view(), name="Home"),
    path("create/",views.Create.as_view(), name="Create"),
    path("view/",views.View_List.as_view(), name="View_List"),
]