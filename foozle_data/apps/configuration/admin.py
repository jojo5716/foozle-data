# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Configuration


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('slack_token', 'slack_notify', 'auto_create_project')

admin.site.register(Configuration, ConfigurationAdmin)