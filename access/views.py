import datetime
from dateutils import relativedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from access.models import ZoneUsage, ToolUsage


@login_required
def index(request):

    zone_usages = ZoneUsage.objects.filter_user(request.user)[:20]

    dt = datetime.datetime.now()

    if 'month' in request.GET:
        month = request.GET['month']
        try:
            dt = datetime.datetime.strptime(month, "%Y-%m")
        except ValueError:
            pass

    previous_month = dt - relativedelta(months=1)
    next_month = dt + relativedelta(months=1)

    if next_month > datetime.datetime.now():
        next_month = None

    period_start = datetime.date(dt.year, dt.month, 1)
    period_end = dt + relativedelta(months=+1, seconds=-1)

    tool_usages, tool_usage_total = ToolUsage.objects\
        .filter_user_month(request.user, dt)

    return render(request, 'access/index.html', locals())
