# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhirfront', '0005_auto_20160803_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='alcoholrisk',
            name='firstscore',
            field=models.FloatField(blank=True, db_column='FirstScore', null=True),
        ),
        migrations.AddField(
            model_name='alcoholrisk',
            name='firststandarddeviation',
            field=models.FloatField(blank=True, db_column='FirstStandardDeviation', null=True),
        ),
        migrations.AddField(
            model_name='alcoholrisk',
            name='secondscore',
            field=models.FloatField(blank=True, db_column='SecondScore', null=True),
        ),
        migrations.AddField(
            model_name='alcoholrisk',
            name='secondstandarddeviation',
            field=models.FloatField(blank=True, db_column='SecondStandardDeviation', null=True),
        ),
        migrations.AddField(
            model_name='alcoholrisk',
            name='thirdscore',
            field=models.FloatField(blank=True, db_column='thirdscore', null=True),
        ),
        migrations.AddField(
            model_name='alcoholrisk',
            name='thirdstandarddeviation',
            field=models.FloatField(blank=True, db_column='ThirdStandardDeviation', null=True),
        ),
    ]
