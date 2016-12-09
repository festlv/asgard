# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0010_auto_20150604_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolusage',
            name='session_length',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
