from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    readonly_fields = ['created_datetime', 'modified_datetime', 'reminder_sent',
                       'payment_received_user', 'payment_received_date']

    list_display = ['user_name', 'amount',
                    'payment_received', 'created_datetime']

admin.site.register(Donation, DonationAdmin)
