# urls.py

from django.conf.urls import patterns, url
from userprofile.views import LogoutView, LoginView

urlpatterns = patterns('',
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^login/$', LoginView.as_view(), name="login"),
)
