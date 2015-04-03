# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20150403_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='access_tools',
            field=models.ManyToManyField(to='access.Tool', db_table=b'userprofile_tool_access'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='access_zones',
            field=models.ManyToManyField(to='access.Zone', db_table=b'userprofile_zone_access'),
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='userprofile',
        ),
    ]
