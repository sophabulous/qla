# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20160103_0416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialMediaIcons',
            new_name='SocialMediaIcon',
        ),
    ]
