from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include("register.urls")),
    path('', include("django.contrib.auth.urls")), 
    path('', include("main.urls")),
    path('api-auth/', include('rest_frameworks.urls')),
    
]
