from django.contrib import admin
from allocator.models import UserProfile, Profile, GoogleProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Profile)
admin.site.register(GoogleProfile)