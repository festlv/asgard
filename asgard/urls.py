from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin
from rest_framework import routers

from access import api_views

api_router = routers.DefaultRouter()
api_router.register(r'cards', api_views.CardViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'asgard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'donations.views.index', name='index'),

    url(r'^accounts/', include('userprofile.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^api/', include(api_router.urls)),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/login/$', RedirectView.as_view(url=settings.LOGIN_URL,
                                                permanent=True,
                                                query_string=True)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('access.admin_urls')),
    url(r'^admin/create_user/', 'userprofile.admin.create_user',
        name='admin_create_user'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
