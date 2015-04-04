from django.db import models
from django.contrib.auth.models import User
from asgard.base_models import TimestampModel


class Card(TimestampModel):
    """ Card is an RFID-based authentication token"""

    user = models.ForeignKey(User)
    serial_number = models.BigIntegerField()
    pin_code = models.IntegerField()

    def __unicode__(self):
        return "%X" % self.serial_number

    class Meta:
        unique_together = ['serial_number', 'is_deleted']


class Zone(TimestampModel):
    """This model corresponds to access zone (e.g. main doors)."""
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class ZoneAccess(TimestampModel):
    """
    This model stores user <> zone relation, which allows users
    access to certain zones
    """
    user = models.ForeignKey(User, related_name="zone_access_set")
    zone = models.ForeignKey(Zone)

    class Meta:
        unique_together = ['user', 'zone']
        verbose_name_plural = 'zone accesses'


class ZoneUsage(TimestampModel):
    card = models.ForeignKey(Card)
    zone = models.ForeignKey(Zone)

    def __unicode__(self):
        return "%s accessed %s" % (self.card, self.zone)


class ZoneAccessLog(TimestampModel):
    serial_number = models.BigIntegerField()
    zone = models.ForeignKey(Zone)
    pin_code = models.IntegerField()
    access_granted = models.BooleanField()


class Tool(TimestampModel):
    """This model corresponds to restricted-access tool (e.g. lasercutter)"""
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class ToolAccess(TimestampModel):
    """
    This model stores user <> tool relation, which allows users
    access to certain tools
    """
    user = models.ForeignKey(User, related_name='tool_access_set')
    tool = models.ForeignKey(Tool)

    class Meta:
        unique_together = ['user', 'tool']
        verbose_name_plural = 'tool accesses'


class ToolUsage(TimestampModel):
    """This model stores which user has used which tool and how long."""
    card = models.ForeignKey(Card)
    tool = models.ForeignKey(Tool)
    usage_start = models.DateTimeField()
    # may not be applicable to all tools
    usage_end = models.DateTimeField(blank=True, null=True)
