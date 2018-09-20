# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='slack_channel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Slack channel to notify'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='slack_token',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Slack token'),
        ),
    ]
