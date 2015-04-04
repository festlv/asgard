# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20150403_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='access_tools',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='access_zones',
        ),
    ]
