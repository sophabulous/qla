# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20160103_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='contributor_area2',
            field=models.CharField(blank=True, default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_area3',
            field=models.CharField(blank=True, default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_biotext',
            field=models.TextField(default=b'This contributor did not provide a bio', max_length=3000),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_position2',
            field=models.CharField(blank=True, default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_position3',
            field=models.CharField(blank=True, default=b' ', max_length=20),
        ),
    ]