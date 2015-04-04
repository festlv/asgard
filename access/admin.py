from django.contrib import admin
from .models import Card, Zone, ZoneUsage, Tool, ToolUsage, \
    ZoneAccessLog, ToolAccess, ZoneAccess
from .forms import CardForm


class TimestampAdmin(admin.ModelAdmin):
    readonly_fields = ['created_datetime', 'modified_datetime']


class CardAdmin(TimestampAdmin):
    form = CardForm
    list_display = ['user', 'serial_number_display', 'is_active', 'is_deleted']

    def serial_number_display(self, obj):
        return "%X" % obj.serial_number
    serial_number_display.short_description = "Serial number"

admin.site.register(Card, CardAdmin)


class ZoneAdmin(TimestampAdmin):
    pass
admin.site.register(Zone, ZoneAdmin)


class ZoneAccessAdmin(TimestampAdmin):
    list_display = ['user', 'zone', 'created_datetime', 'is_active']
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
                    'usage_length_display']

    def card_user_display(self, obj):
        return obj.card.user
    card_user_display.short_description = "User"

    def usage_length_display(self, obj):
        if obj.usage_end:
            td = obj.usage_end - obj.usage_start
            hours, remainder = divmod(td.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            return '%d:%02d:%02d' % (hours, minutes, seconds)
        return 'ongoing'

    usage_length_display.short_description = 'Duration'


class ToolAccessAdmin(TimestampAdmin):
    list_display = ('user', 'tool', 'created_datetime', 'is_active')
    list_filter = ('tool', 'is_active', 'is_deleted')
admin.site.register(ToolAccess, ToolAccessAdmin)


admin.site.register(ToolUsage, ToolUsageAdmin)
