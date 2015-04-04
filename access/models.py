from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User

from asgard.base_models import SoftDeleteModel, TimestampModel


class Card(SoftDeleteModel):
    """ Card is an RFID-based authentication token"""

    user = models.ForeignKey(User)
    serial_number = models.BigIntegerField()
    pin_code = models.IntegerField()

    def __unicode__(self):
        return "%X" % self.serial_number

    class Meta:
        unique_together = ['serial_number', 'is_deleted']


class Zone(SoftDeleteModel):
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


class Tool(SoftDeleteModel):
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

    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True,
                               help_text="This field is filled-in \
                                automatically upon save",
                               null=True)

    def save(self, *args, **kwargs):
        """
        Calculates cost of this instance of tool usage from user's
        level and corresponding tool price entry.
        """
        self.cost = None
        if self.usage_end:
            td = self.usage_end - self.usage_start
            hours = Decimal(td.total_seconds() / 3600.0)

            # in theory, there might be a case where user's profile
            # does not exist
            if self.card.user.user_profile:
                try:
                    tool_price = UserLevelToolPrice.objects.get(
                        user_level=self.card.user.user_profile.level,
                        tool=self.tool)

                    self.cost = hours * tool_price.price
                except UserLevelToolPrice.DoesNotExist:
                    pass

        super(ToolUsage, self).save(*args, **kwargs)


class UserLevel(SoftDeleteModel):
    """
    UserLevel is used to group users and assign pricing rules for use
    of tools
    """
    title = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.title


class UserLevelToolPrice(TimestampModel):
    """
    This model stores tool usage prices for each user level.
    Price is per hour of tool's usage.
    """
    tool = models.ForeignKey(Tool)
    user_level = models.ForeignKey(UserLevel)
    price = models.DecimalField(max_digits=5, decimal_places=2,
                                help_text="Per hour")

    def __unicode__(self):
        return "%s price for %s: %.2f" % (
            self.user_level, self.tool, self.price)

    class Meta:
        unique_together = ['tool', 'user_level']
