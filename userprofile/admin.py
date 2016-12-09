import random

from django.contrib import admin
from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from userprofile.models import UserProfile
from userprofile.forms import CreateUserForm
from access.models import ZoneAccessLog, Card, ZoneAccess, ToolAccess
from access.forms import CardForm


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
    readonly_fields = ['created_datetime', 'modified_datetime']


class ZoneInline(admin.TabularInline):
    model = ZoneAccess
    readonly_fields = ['created_datetime', 'modified_datetime']
    extra = 1


class ToolInline(admin.TabularInline):
    model = ToolAccess
    readonly_fields = ['created_datetime', 'modified_datetime']
    extra = 1


class CardInline(admin.TabularInline):
    model = Card
    form = CardForm
    readonly_fields = ['created_datetime', 'modified_datetime']
    extra = 1


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, CardInline, ToolInline, ZoneInline ]
    list_display = ['username', 'level_display',
                    'is_active', 'is_staff']

    def level_display(self, obj):
        if obj.user_profile:
            return obj.user_profile.level
        else:
            return "(None)"
    level_display.short_description = "Level"

    # disables deletion form database
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)


def get_username(email):
    """
    Creates a non-existing username from e-mail address.
    @TODO: This introduces a race condition when two users are
    being created simultaneously.
    """

    found_free = False
    username = email.split('@')[0]
    i = 0
    while not found_free:
        test_name = "%s-%d" % (username, i)
        if User.objects.filter(
            username__iexact=test_name
        ).count() == 0:
            username = test_name
            break
        i += 1

    return username


@transaction.atomic
def create_user(request):
    """
    Creates a user, it's profile and related access card entry in one
    page
    """
    # retrieve last 5 failed logins, so that card number can be deduced
    last_failed_access_attempts = ZoneAccessLog.objects\
        .filter(access_granted=False)\
        .order_by('-created_datetime')[:5]

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #
        form = CreateUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # try to save the data
            username = get_username(form.cleaned_data['email'])
            password = User.objects.make_random_password()
            pin_code = random.randint(999, 9999)

            u = User.objects.create_user(
                username=username, email=form.cleaned_data['email'],
                password=password, first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'])

            up = UserProfile.objects.create(
                user=u, phone_number=form.cleaned_data['phone_number'],
                level=form.cleaned_data['level'])

            for z in form.cleaned_data['zone_access']:
                u.zone_access_set.create(zone=z)

            for t in form.cleaned_data['tool_access']:
                u.tool_access_set.create(tool=t)

            card = Card.objects.create(
                user=u, pin_code=pin_code,
                serial_number=form.cleaned_data['card_serial_number'])

            return render(request, 'userprofile/create_user_success.html',
                          locals())

    else:
        form = CreateUserForm()

    return render(request, 'userprofile/create_user.html', locals())
