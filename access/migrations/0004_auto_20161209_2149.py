# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_userlevel_send_donation_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='toolaccess',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='toolaccess',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='toolusage',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='toolusage',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='userleveltoolprice',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='userleveltoolprice',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zoneaccess',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zoneaccess',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zoneaccesslog',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zoneaccesslog',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zoneusage',
            name='created_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created datetime', blank=True),
        ),
        migrations.AlterField(
            model_name='zoneusage',
            name='modified_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified datetime', blank=True),
        ),
    ]
