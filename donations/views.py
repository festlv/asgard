from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Donation
from access.models import ZoneAccessLog


@login_required
def index(request):

    donations = Donation.objects.user_donations(request.user)[20:]

    zone_access = ZoneAccessLog.objects.filter_user(request.user)[:20]

    return render(request, 'donations/index.html', locals())
