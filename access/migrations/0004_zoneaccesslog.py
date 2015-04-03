# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_auto_20150403_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneAccessLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('serial_number', models.BigIntegerField()),
                ('pin_code', models.IntegerField()),
                ('access_granted', models.BooleanField()),
                ('zone', models.ForeignKey(to='access.Zone')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
