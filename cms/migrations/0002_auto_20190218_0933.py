# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 09:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='block_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.Block_Location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.NewsType'),
        ),
        migrations.AlterField(
            model_name='news',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.State'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.District'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.State'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subnav',
            name='nav',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.Nav'),
        ),
    ]