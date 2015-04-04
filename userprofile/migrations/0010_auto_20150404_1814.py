# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_levels(apps, schema_editor):
    UserLevel = apps.get_model("access", "UserLevel")
    a = UserLevel.objects.create(title="Level A")
    UserLevel.objects.create(title="Level B")
    UserLevel.objects.create(title="Level C")

    UserProfile = apps.get_model("userprofile", "UserProfile")
    for up in UserProfile.objects.all():
        up.level = a
        up.save()


def remove_levels(apps, schema_editor):

    UserProfile = apps.get_model("userprofile", "UserProfile")
    for up in UserProfile.objects.all():
        up.level = None
        up.save()

    UserLevel = apps.get_model("access", "UserLevel")
    UserLevel.objects.get(title="Level A").delete()
    UserLevel.objects.get(title="Level B").delete()
    UserLevel.objects.get(title="Level C").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_userprofile_level'),
        ('access', '0007_auto_20150404_1806'),
    ]

    operations = [
        migrations.RunPython(create_levels, remove_levels)
    ]
