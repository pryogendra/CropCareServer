from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path("posts/",views.post,name='post'),
    path("profile/",views.profile,name='profile'),
    path('updateprofile/',views.updateprofile,name='updateprofile'),

    #demo URL
    # path('upload/',views.upload_image,name='upload'),
    # path('getImage/',views.get_image,name='get_image'),
]
