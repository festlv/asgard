# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0006_auto_20150404_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserLevelToolPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('tool', models.ForeignKey(to='access.Tool')),
                ('user_level', models.ForeignKey(to='access.UserLevel')),
            ],
        ),
        migrations.AlterModelOptions(
            name='toolaccess',
            options={'verbose_name_plural': 'tool accesses'},
        ),
        migrations.AlterModelOptions(
            name='zoneaccess',
            options={'verbose_name_plural': 'zone accesses'},
        ),
        migrations.AlterField(
            model_name='zoneaccess',
            name='user',
            field=models.ForeignKey(related_name='zone_access_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userleveltoolprice',
            unique_together=set([('tool', 'user_level')]),
        ),
    ]
