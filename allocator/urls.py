from django.conf.urls import url,include,patterns
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^api/$', views.api_examples, name='api'),
    url(r'^google_login/$', views.google_login, name='google_login'),
    url(r'^google/$', views.googlePlus, name='googlePlus'),
    url(r'^admin/', include(admin.site.urls)),

    
]
