# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_weeklyvignette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyvignette',
            name='wv_content',
            field=models.TextField(max_length=10000),
        ),
    ]