# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    ProjectTypes,
    Account,
    Project,
    UserProfile,
    Data
)

admin.site.register(ProjectTypes)
admin.site.register(Account)
admin.site.register(Project)
admin.site.register(UserProfile)
admin.site.register(Data)