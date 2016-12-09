from django.db import models
from django.conf import settings

from djmoney.models.fields import MoneyField

from django.contrib.auth.models import User

from asgard.base_models import SoftDeleteModel, BaseSoftDeleteManager


class DonationManager(BaseSoftDeleteManager):
    def user_donations(self, user):

        return self.all_active().filter(
            user=user,
            payment_received=True).order_by("-payment_received_date")

class Donation(SoftDeleteModel):

    user = models.ForeignKey(User, related_name='donations')
    amount = MoneyField(max_digits=10, decimal_places=2,
                        default_currency=settings.CURRENCIES[0])

    reminder_sent = models.BooleanField(default=False, blank=True)

    payment_received = models.BooleanField(default=False, blank=True)
    payment_reference = models.CharField(max_length=100, blank=True)
    payment_received_date = models.DateTimeField(blank=True, null=True)
    payment_received_user = models.ForeignKey(User, blank=True, null=True,
                                              related_name='donations_accepted')

    objects = DonationManager()
