import datetime
from dateutils import relativedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Donation
from access.models import ZoneUsage

@login_required
def index(request):

    donations = Donation.objects.user_donations(request.user)[20:]

    zone_usages = ZoneUsage.objects.filter_user(request.user)[:20]

    return render(request, 'donations/index.html', locals())
