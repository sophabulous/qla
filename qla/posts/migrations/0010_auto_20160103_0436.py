# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20160103_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaicon',
            name='socialmediaicon_link',
            field=models.CharField(default=b'#', max_length=30),
        ),
    ]