# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20160104_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_cover',
            field=models.CharField(default=b'fpo_4x3.PNG', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='post_thumb',
            field=models.CharField(default=b'fpo_square.PNG', max_length=30),
        ),
    ]
