from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'asgard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'donations.views.index', name='index'),

    url(r'^accounts/', include('userprofile.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),


    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('access.admin_urls')),
    url(r'^admin/create_user/', 'userprofile.admin.create_user', name='admin_create_user'),
]
