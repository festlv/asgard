# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djmoney.models.fields
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_auto_20161209_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlevel',
            name='can_open_doors',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='recommended_donation',
            field=djmoney.models.fields.MoneyField(default=Decimal('0.0'), max_digits=10, decimal_places=2, default_currency=b'EUR'),
        ),
    ]
