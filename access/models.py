from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    """ Card is an RFID-based authentication token"""

    user = models.ForeignKey(User)
    serial_number = models.BigIntegerField()
    pin_code = models.IntegerField()


class Zone(models.Model):
    """This model corresponds to access zone (e.g. main doors)."""
    title = models.CharField(max_length=50)


class Tool(models.Model):
    """This model corresponds to restricted-access tool (e.g. lasercutter)"""
    title = models.CharField(max_length=50)
