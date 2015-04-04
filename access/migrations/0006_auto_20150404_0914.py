# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('access', '0005_auto_20150403_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('tool', models.ForeignKey(to='access.Tool')),
                ('user', models.ForeignKey(related_name='tool_access_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ZoneAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(to='access.Zone')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='zoneaccess',
            unique_together=set([('user', 'zone')]),
        ),
        migrations.AlterUniqueTogether(
            name='toolaccess',
            unique_together=set([('user', 'tool')]),
        ),
    ]
