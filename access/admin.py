from django.contrib import admin
from access.models import Card, Zone, ZoneUsage, Tool, ToolUsage


class TimestampAdmin(admin.ModelAdmin):
    readonly_fields = ['created_datetime', 'modified_datetime']


class CardAdmin(TimestampAdmin):
    pass

admin.site.register(Card, CardAdmin)


class ZoneAdmin(TimestampAdmin):
    pass
admin.site.register(Zone, ZoneAdmin)


class ZoneUsageAdmin(TimestampAdmin):
    pass
admin.site.register(ZoneUsage, ZoneUsageAdmin)


class ToolAdmin(TimestampAdmin):
    pass
admin.site.register(Tool, ToolAdmin)


class ToolUsageAdmin(TimestampAdmin):
    pass
admin.site.register(ToolUsage, ToolUsageAdmin)
