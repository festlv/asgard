from django.db import models


class ZoneUsageManager(models.Manager):

    def filter_user(self, user):
        """Return QuerySet filtered by user,"""
        return self.filter(card__user=user).order_by('-created_datetime')


class ZoneAccessLogManager(models.Manager):

    def filter_user(self, user):
        """Return QuerySet filtered by user"""
        return self.filter(card__user=user, access_granted=True).order_by('-created_datetime')


class ToolUsageManager(models.Manager):

    def filter_user_month(self, user, date):
        """
        Return QuerySet filtered by user and month,
        aggregates the sum and displays it.
        Date should be python's date object.

        Returns a tuple of QuerySet and total usage cost for this QuerySet.
        """

        qs = self.filter(card__user=user, modified_datetime__year=date.year,
                         modified_datetime__month=date.month)

        total = qs.aggregate(models.Sum('cost'))

        return (qs, total)
