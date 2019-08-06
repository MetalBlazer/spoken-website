# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creation', '0014_auto_20190703_1146'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contributorrole',
            unique_together=set([('user', 'tutorial_detail', 'language')]),
        ),
    ]