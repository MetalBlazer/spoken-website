# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-21 05:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creation', '0018_tutorialduration_created'),
        ('events', '0044_auto_20200718_1203'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('gender', models.CharField(choices=[('', '--- Gender ---'), ('M', 'Male'), ('F', 'Female'), ('O', "Don't wish to disclose")], max_length=6, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.AcademicCenter')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.Department')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('', '-----'), ('FDP', 'FDP'), ('SDP', 'SDP'), ('Workshop', 'Workshop')], max_length=50)),
                ('event_name', models.CharField(max_length=200)),
                ('event_start_date', models.DateField(default=datetime.datetime.now)),
                ('event_end_date', models.DateField(default=datetime.datetime.now)),
                ('event_coordinator_name', models.CharField(max_length=200)),
                ('event_coordinator_email', models.EmailField(max_length=254, null=True)),
                ('event_coordinator_contact_no', models.CharField(max_length=100, null=True)),
                ('registartion_start_date', models.DateField(default=datetime.datetime.now)),
                ('registartion_end_date', models.DateField(default=datetime.datetime.now)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('Language_of_workshop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='creation.Language')),
                ('entry_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('foss', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='creation.FossCategory')),
                ('host_college', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.AcademicCenter')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.State')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training.TrainingEvents'),
        ),
        migrations.AddField(
            model_name='participant',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.State'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
