# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20150403_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='access_tools',
            field=models.ManyToManyField(to='access.Tool', db_table=b'user_profile_tool_access'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='access_zones',
            field=models.ManyToManyField(to='access.Zone', db_table=b'user_profile_zone_access'),
        ),
    ]
