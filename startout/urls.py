from django.conf.urls import patterns, include, url
from django.contrib import admin

from allocator import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'startout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.index, name='index'),
    url(r'^allocator/', include('allocator.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
