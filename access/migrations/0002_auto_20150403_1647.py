# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('usage_start', models.DateTimeField()),
                ('usage_end', models.DateTimeField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ZoneUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='card',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AddField(
            model_name='card',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='card',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='card',
            name='modified_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tool',
            name='modified_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AddField(
            model_name='zone',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AddField(
            model_name='zone',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='zone',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='zone',
            name='modified_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AddField(
            model_name='zoneusage',
            name='card',
            field=models.ForeignKey(to='access.Card'),
        ),
        migrations.AddField(
            model_name='zoneusage',
            name='zone',
            field=models.ForeignKey(to='access.Zone'),
        ),
        migrations.AddField(
            model_name='toolusage',
            name='card',
            field=models.ForeignKey(to='access.Card'),
        ),
        migrations.AddField(
            model_name='toolusage',
            name='tool',
            field=models.ForeignKey(to='access.Tool'),
        ),
    ]
