# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20160103_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='contributor_image',
            field=models.CharField(default=b'img', max_length=30),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_area1',
            field=models.CharField(default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_area2',
            field=models.CharField(default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_area3',
            field=models.CharField(default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_position1',
            field=models.CharField(default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_position2',
            field=models.CharField(default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_position3',
            field=models.CharField(default=b' ', max_length=20),
        ),
    ]
