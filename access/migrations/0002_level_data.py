# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_levels(apps, schema_editor):
    UserLevel = apps.get_model("access", "UserLevel")
    a = UserLevel.objects.create(title="Level A", recommended_donation=5)
    UserLevel.objects.create(title="Level B", recommended_donation=20)
    UserLevel.objects.create(title="Level C", recommended_donation=50)

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
        ('userprofile', '0001_initial'),
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_levels, remove_levels)
    ]
