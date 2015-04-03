# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_auto_20150403_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolusage',
            name='usage_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
