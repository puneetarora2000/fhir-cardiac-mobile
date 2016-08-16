# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhirfront', '0009_auto_20160803_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='weightrisk',
            name='thirdstandarddeviationscore',
            field=models.FloatField(blank=True, db_column='ThirdStandardDeviationScore', null=True),
        ),
        migrations.AlterField(
            model_name='weightrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Same', 'Same')], default='Same', max_length=20),
        ),
    ]
