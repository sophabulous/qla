# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160103_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='contributor_biotext',
            field=models.CharField(default=b'bio', max_length=3000),
        ),
    ]