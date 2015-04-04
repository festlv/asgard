# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0007_auto_20150404_1806'),
        ('userprofile', '0008_auto_20150404_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.ForeignKey(to='access.UserLevel', null=True),
        ),
    ]
