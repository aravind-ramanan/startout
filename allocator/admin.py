from django.contrib import admin
from allocator.models import UserProfile, Profile, GoogleProfile, Project, UserDetails

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Profile)
admin.site.register(GoogleProfile)
admin.site.register(Project)
admin.site.register(UserDetails)