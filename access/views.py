from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from access.models import ZoneUsage, ToolUsage


@login_required
def index(request):
    zone_usages = ZoneUsage.objects.filter_user(request.user)[:20]

    tool_usages, tool_usage_total = ToolUsage.objects\
        .filter_user_month(request.user, date.today())

    return render(request, 'access/index.html', locals())
