import smtplib

from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from donations.models import Donation


class Command(BaseCommand):
    args = ''
    help = 'Sends e-mails reminding about due donation'

    def handle(self, *args, **options):
        users = User.objects.filter(is_active=True)

        for user in users:
            # render e-mail template
            level = user.user_profile.level
            # don't send reminders for some levels
            if not level.send_donation_reminder:
                continue
            recommended_amount = level.recommended_donation
            context = {
                'user': user,
                'recommended_amount': recommended_amount,
                'level': level
                       }
            html = render_to_string('donations/donation_reminder.html', context)
            text = render_to_string('donations/donation_reminder.txt', context)
            subject = render_to_string(
                'donations/donation_reminder_subject.txt', context)
            # strip newlines
            subject = subject.strip()

            msg = EmailMultiAlternatives(subject, text,
                                         settings.DEFAULT_FROM_EMAIL,
                                         [user.email])
            msg.attach_alternative(html, 'text/html')
            msg.content_subtype = 'html'

            reminder_sent = False

            try:
                msg.send()
                reminder_sent = True
            except smtplib.SMTPException:
                pass

            d = Donation()
            d.amount = recommended_amount
            d.reminder_sent = reminder_sent
            d.user = user

            d.save()
            print("Sent reminder to: %s" % (user.email, ))
