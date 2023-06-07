from django.contrib import admin
from django.urls import path,include # yeni ekledik include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('user/', include("users.urls")),
    

]
