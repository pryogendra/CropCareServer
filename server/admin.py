from django.contrib import admin
from .models import *
from django.contrib.admin.sites import site
from django.contrib.admin import AdminSite

admin.site.site_title = "CropCare Admin"
admin.site.site_header = "Welcome to CropCare Admin Panel"
admin.site.index_title = "Dashboard"

#Display the custom columns
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('location','mobile')
#admin.site.register(UserProfile,ProfileAdmin)


admin.site.register(UserProfile)
admin.site.register([Post,Notification])
admin.site.register(Govt_Scheme)
admin.site.register(Shopping)
admin.site.register([Contactus,FeedBack])
