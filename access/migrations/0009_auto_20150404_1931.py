# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0008_auto_20150404_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolusage',
            name='cost',
            field=models.DecimalField(help_text=b'This field is filled-in                                 automatically upon save', null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='userleveltoolprice',
            name='price',
            field=models.DecimalField(help_text=b'Per hour', max_digits=5, decimal_places=2),
        ),
    ]
