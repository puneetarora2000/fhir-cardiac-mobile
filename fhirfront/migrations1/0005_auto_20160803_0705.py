# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhirfront', '0004_agerisk_thirdscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agerisk',
            name='thirdscore',
            field=models.FloatField(blank=True, db_column='thirdscore', null=True),
        ),
    ]
