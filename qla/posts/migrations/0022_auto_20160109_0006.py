# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 05:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20160108_2352'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blah',
            new_name='WeeklyVignette',
        ),
    ]
