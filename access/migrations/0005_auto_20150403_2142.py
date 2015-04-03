# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_zoneaccesslog'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='card',
            unique_together=set([('serial_number', 'is_deleted')]),
        ),
    ]
