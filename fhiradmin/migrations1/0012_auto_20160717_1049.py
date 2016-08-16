# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-17 05:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fhiradmin', '0011_auto_20160716_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodpressurereading',
            name='FatInTake',
        ),
        migrations.RemoveField(
            model_name='bloodpressurereading',
            name='FoodSupliment',
        ),
        migrations.RemoveField(
            model_name='bloodpressurereading',
            name='WhichDrink',
        ),
        migrations.AddField(
            model_name='bloodpressurereading',
            name='DiastolicReading',
            field=models.IntegerField(default='90', verbose_name='Systolic Reading'),
        ),
        migrations.AddField(
            model_name='bloodpressurereading',
            name='LastDateOfTest',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 17, 5, 19, 5, 115000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodpressurereading',
            name='SystolicReading',
            field=models.IntegerField(default='90', verbose_name='Systolic Reading'),
        ),
    ]