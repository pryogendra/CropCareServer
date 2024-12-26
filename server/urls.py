from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path("posts/",views.post,name='post'),
    path("profile/",views.profile,name='profile'),
    path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('schemes/',views.schemes,name='schemes'),
    path('schemedetail/',views.schemedetail,name='schemedetail'),


    # path('scheme/',views.add_scheme,name='add_scheme'),
    #demo URL
    # path('upload/',views.upload_image,name='upload'),
    # path('getImage/',views.get_image,name='get_image'),
]
