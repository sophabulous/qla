# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 04:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20160106_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklyvignette',
            old_name='wv_author',
            new_name='weeklyvignette_author',
        ),
        migrations.RenameField(
            model_name='weeklyvignette',
            old_name='wv_content',
            new_name='weeklyvignette_content',
        ),
        migrations.RenameField(
            model_name='weeklyvignette',
            old_name='wv_cover',
            new_name='weeklyvignette_cover',
        ),
        migrations.RenameField(
            model_name='weeklyvignette',
            old_name='wv_date',
            new_name='weeklyvignette_date',
        ),
        migrations.RenameField(
            model_name='weeklyvignette',
            old_name='wv_excerpt',
            new_name='weeklyvignette_excerpt',
        ),
        migrations.RenameField(
            model_name='weeklyvignette',
            old_name='wv_title',
            new_name='weeklyvignette_title',
        ),
    ]
