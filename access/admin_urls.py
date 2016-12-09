
from django.conf.urls import url

from .admin import tool_usage_report

urlpatterns = [
    url(r'^reports/tool-usage/$', tool_usage_report, name="admin_tool_usage"),

]
