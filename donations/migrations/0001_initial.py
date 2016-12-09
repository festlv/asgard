# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from decimal import Decimal
import djmoney.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('amount_currency', djmoney.models.fields.CurrencyField(default=b'EUR', max_length=3, editable=False, choices=[(b'EUR', 'Euro')])),
                ('reminder_sent', models.BooleanField(default=False)),
                ('amount', djmoney.models.fields.MoneyField(default=Decimal('0.0'), max_digits=10, decimal_places=2, default_currency=b'EUR')),
                ('payment_received', models.BooleanField(default=False)),
                ('payment_reference', models.CharField(max_length=100, blank=True)),
                ('payment_received_date', models.DateTimeField(null=True, blank=True)),
                ('payment_received_user', models.ForeignKey(related_name='donations_accepted', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='donations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
