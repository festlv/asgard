from django.db import models
from django.contrib.auth.models import User
from asgard.base_models import TimestampModel


class Card(TimestampModel):
    """ Card is an RFID-based authentication token"""

    user = models.ForeignKey(User)
    serial_number = models.BigIntegerField()
    pin_code = models.IntegerField()

    def __unicode__(self):
        return hex(self.serial_number)


class Zone(TimestampModel):
    """This model corresponds to access zone (e.g. main doors)."""
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class ZoneUsage(TimestampModel):
    card = models.ForeignKey(Card)
    zone = models.ForeignKey(Zone)

    def __unicode__(self):
        return "%s accessed %s" % (self.card, self.zone)


class Tool(TimestampModel):
    """This model corresponds to restricted-access tool (e.g. lasercutter)"""
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class ToolUsage(TimestampModel):
    """This model stores which user has used which tool and how long."""
    card = models.ForeignKey(Card)
    tool = models.ForeignKey(Tool)
    usage_start = models.DateTimeField()
    # may not be applicable to all tools
    usage_end = models.DateTimeField(blank=True)
