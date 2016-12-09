# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_level_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlevel',
            name='send_donation_reminder',
            field=models.BooleanField(default=True),
        ),
    ]
