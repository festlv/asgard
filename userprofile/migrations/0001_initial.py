# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('level', models.ForeignKey(to='access.UserLevel')),
                ('user', models.OneToOneField(related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userprofile',
            },
        ),
    ]
