# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20150403_1809'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together=set([('user', 'is_deleted')]),
        ),
    ]
