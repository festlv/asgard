from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone


class TimestampModel(models.Model):
    """
    Base timestamp model. Adds the following fields for model:
        * created_datetime
        * modified_datetime
    """
    created_datetime = models.DateTimeField(
        _('created datetime'), blank=True, default=timezone.now)
    modified_datetime = models.DateTimeField(
        _('modified datetime'), blank=True, default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_datetime = timezone.now()
        self.modified_datetime = timezone.now()

        super(TimestampModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class SoftDeleteModel(TimestampModel):
    """
    Abstract model which adds soft-delete fields:
        * is_active
        * is_deleted
    """
    is_active = models.BooleanField(default=True, blank=True)
    is_deleted = models.BooleanField(default=False, blank=True)

    class Meta:
        abstract = True


class BaseSoftDeleteManager(models.Manager):

    def all_active(self):
        return self.filter(is_deleted=False, is_active=True)
