from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include("register.urls")),
    path('', include("django.contrib.auth.urls")), 
    path('', include("main.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/')
    
]
