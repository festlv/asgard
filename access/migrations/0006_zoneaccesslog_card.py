# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0005_auto_20161215_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoneaccesslog',
            name='card',
            field=models.ForeignKey(blank=True, to='access.Card', null=True),
        ),
    ]
