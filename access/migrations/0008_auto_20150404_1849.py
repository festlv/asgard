# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0007_auto_20150404_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolaccess',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='toolaccess',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='toolusage',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='toolusage',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='userleveltoolprice',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userleveltoolprice',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='zoneaccess',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='zoneaccess',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='zoneaccesslog',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='zoneaccesslog',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='zoneusage',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='zoneusage',
            name='is_deleted',
        ),
    ]
