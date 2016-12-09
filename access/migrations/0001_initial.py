# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from decimal import Decimal
from django.conf import settings
import djmoney.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('serial_number', models.BigIntegerField()),
                ('pin_code', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ToolAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('tool', models.ForeignKey(to='access.Tool')),
                ('user', models.ForeignKey(related_name='tool_access_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'tool accesses',
            },
        ),
        migrations.CreateModel(
            name='ToolUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('session_length', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cost', models.DecimalField(help_text=b'This field is filled-in                                 automatically upon save', null=True, max_digits=10, decimal_places=2, blank=True)),
                ('card', models.ForeignKey(to='access.Card')),
                ('tool', models.ForeignKey(to='access.Tool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('recommended_donation_currency', djmoney.models.fields.CurrencyField(default=b'EUR', max_length=3, editable=False, choices=[(b'EUR', 'Euro')])),
                ('recommended_donation', djmoney.models.fields.MoneyField(default=Decimal('0.0'), default_currency=b'EUR', max_digits=10, decimal_places=2, blank=True)),
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
                ('price', models.DecimalField(help_text=b'Per hour', max_digits=5, decimal_places=2)),
                ('tool', models.ForeignKey(to='access.Tool')),
                ('user_level', models.ForeignKey(to='access.UserLevel')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ZoneAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('user', models.ForeignKey(related_name='zone_access_set', to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(to='access.Zone')),
            ],
            options={
                'verbose_name_plural': 'zone accesses',
            },
        ),
        migrations.CreateModel(
            name='ZoneAccessLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='created datetime', blank=True)),
                ('modified_datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='modified datetime', blank=True)),
                ('serial_number', models.BigIntegerField()),
                ('pin_code', models.IntegerField()),
                ('access_granted', models.BooleanField()),
                ('zone', models.ForeignKey(to='access.Zone')),
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
                ('card', models.ForeignKey(to='access.Card')),
                ('zone', models.ForeignKey(to='access.Zone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='zoneaccess',
            unique_together=set([('user', 'zone')]),
        ),
        migrations.AlterUniqueTogether(
            name='userleveltoolprice',
            unique_together=set([('tool', 'user_level')]),
        ),
        migrations.AlterUniqueTogether(
            name='toolaccess',
            unique_together=set([('user', 'tool')]),
        ),
        migrations.AlterUniqueTogether(
            name='card',
            unique_together=set([('serial_number', 'is_deleted')]),
        ),
    ]
