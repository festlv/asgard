from django.contrib import admin
from django.shortcuts import render, get_object_or_404

from asgard.utils import format_currency

from django.contrib.auth.models import User

from .models import Card, Zone, ZoneUsage, Tool, ToolUsage, \
    ZoneAccessLog, ToolAccess, ZoneAccess, UserLevel, \
    UserLevelToolPrice
from .forms import CardForm


class TimestampAdmin(admin.ModelAdmin):
    readonly_fields = ['created_datetime', 'modified_datetime']


class CardAdmin(TimestampAdmin):
    form = CardForm
    list_display = ['user_first_name', 'user_last_name',
                    'serial_number_display', 'is_active', 'is_deleted']
    readonly_fields = ['user', 'created_datetime', 'modified_datetime']

    def serial_number_display(self, obj):
        return "%X" % obj.serial_number
    serial_number_display.short_description = "Serial number"

admin.site.register(Card, CardAdmin)


class ZoneAdmin(TimestampAdmin):
    pass
admin.site.register(Zone, ZoneAdmin)


class ZoneAccessAdmin(TimestampAdmin):
    list_display = ['user', 'zone', 'created_datetime']
admin.site.register(ZoneAccess, ZoneAccessAdmin)


class ZoneAccessLogAdmin(TimestampAdmin):
    list_display = ['zone', 'serial_number_display', 'access_granted',
                    'created_datetime']

    def serial_number_display(self, obj):
        return "%X" % obj.serial_number
    serial_number_display.short_description = "Serial number"

admin.site.register(ZoneAccessLog, ZoneAccessLogAdmin)


class ZoneUsageAdmin(TimestampAdmin):
    list_display = ['zone', 'card', 'card_user_display', 'created_datetime']

    def card_user_display(self, obj):
        return obj.card.user
    card_user_display.short_description = "User"

admin.site.register(ZoneUsage, ZoneUsageAdmin)


class ToolAdmin(TimestampAdmin):
    pass
admin.site.register(Tool, ToolAdmin)


class ToolUsageAdmin(TimestampAdmin):
    list_display = ['tool', 'card', 'card_user_display',
                    'usage_length_display', 'cost_display']

    readonly_fields = ['cost', 'created_datetime', 'modified_datetime']

    def card_user_display(self, obj):
        return obj.card.user
    card_user_display.short_description = "User"

    def cost_display(self, obj):
        return format_currency(obj.cost)
    cost_display.short_description = "Cost"

    def usage_length_display(self, obj):
        if obj.session_length:
            hours, remainder = divmod(obj.session_length, 3600)
            minutes, seconds = divmod(remainder, 60)
            return '%d:%02d:%02d' % (hours, minutes, seconds)
        return 'ongoing'

    usage_length_display.short_description = 'Duration'

admin.site.register(ToolUsage, ToolUsageAdmin)


class ToolAccessAdmin(TimestampAdmin):
    list_display = ('user', 'tool', 'created_datetime')

admin.site.register(ToolAccess, ToolAccessAdmin)


class UserLevelAdmin(TimestampAdmin):
    list_display = ('title', 'recommended_donation', 'send_donation_reminder',
                    'is_active', 'is_deleted')

admin.site.register(UserLevel, UserLevelAdmin)


class UserLevelTPAdmin(TimestampAdmin):
    list_display = ('tool', 'user_level', 'price')

admin.site.register(UserLevelToolPrice, UserLevelTPAdmin)


def user_tool_usage_report(requests, user_pk, date_from=None, date_to=None):
    """
    View tool usage by user.
    """
    user = get_object_or_404(User, pk=user_pk)


def tool_usage_report(request, tool_pk=None, date_from=None, date_to=None):
    """
    View for tool usage reports, showing usage by tool.

    Contains a filter for date range.
    """
    raise NotImplemented("This feature has not been implemented")

    tools = Tool.objects.all_active()

    # get a list of users and sum of their cost related
    # for t in tools:
    #    users = User.objects.filter(card_set

    return render(request, 'access/admin/tool_usage_report.html', locals())
