# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20150403_1647'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='user_profile',
        ),
    ]