from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('emailregister/', views.emailregister, name='emailregister'),
    path('forgetpassword/',views.forgetpassword, name='forgetpassword'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path("posts/", views.post, name='post'),
    path("profile/", views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('schemes/', views.schemes,name='schemes'),
    path('schemedetail/', views.schemedetail, name='schemedetail'),
    path('shopping/', views.shopping, name='shopping'),
    path('contactus/', views.contactus, name='contactus'),
    path('feedback/', views.feedback, name='feedback'),



    # path('scheme/',views.add_scheme,name='add_scheme'),
    #demo URL
    # path('upload/',views.upload_image,name='upload'),
    # path('getImage/',views.get_image,name='get_image'),
    path('sent/',views.sent,name='sent'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
