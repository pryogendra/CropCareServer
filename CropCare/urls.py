from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('server_admin/', admin.site.urls),
    path('abcd/',include('server.urls'))
]
