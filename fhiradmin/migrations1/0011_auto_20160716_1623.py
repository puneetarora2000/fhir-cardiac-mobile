# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-16 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhiradmin', '0010_auto_20160716_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='Weight',
            field=models.IntegerField(default='50', verbose_name='Weight in Kgs'),
        ),
    ]
