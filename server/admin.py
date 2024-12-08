from django.contrib import admin
from .models import UserProfile
from django.contrib.admin.sites import site

admin.site.register(UserProfile)
