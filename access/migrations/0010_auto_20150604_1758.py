# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0009_auto_20150404_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolusage',
            name='usage_end',
        ),
        migrations.RemoveField(
            model_name='toolusage',
            name='usage_start',
        ),
        migrations.AddField(
            model_name='toolusage',
            name='session_length',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
