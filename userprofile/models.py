from django.db import models
from django.contrib.auth.models import User
from asgard.base_models import TimestampModel
from access.models import UserLevel


class UserProfile(TimestampModel):
    """User profile model may contain custom fields for users
    see: https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
    """

    user = models.OneToOneField(User, related_name='user_profile')
    level = models.ForeignKey(UserLevel)
    phone_number = models.CharField(max_length=20)

    def __unicode__(self):
        return "Userprofile for %s" % self.user

    class Meta:
        db_table = "userprofile"
