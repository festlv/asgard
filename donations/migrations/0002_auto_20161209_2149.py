# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
    ]
