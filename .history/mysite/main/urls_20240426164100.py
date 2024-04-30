from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("",views.home.as_view(), name="home"),
    path("create/",views.create.as_view(), name="create"),
    path("view/",views.View.as_view(), name="view"),
]