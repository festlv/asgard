from django.db import models
from django.contrib.auth.models import User
from access.models import Zone, Tool


class UserProfile(models.Model):
    """User profile model may contain custom fields for users
    see: https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
    """

    user = models.OneToOneField(User)
    phone_number = models.TextField(max_length=20)
    access_zones = models.ManyToManyField(Zone)
    access_tools = models.ManyToManyField(Tool)
