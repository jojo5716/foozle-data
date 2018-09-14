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
### ============== ProjectTypes ============== ###
class ProjectTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ProjectTypes, ProjectTypesAdmin)
### ============== ProjectTypes ============== ###

### ============== [END] Account ============== ###
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'print_projects_name')

    def print_projects_name(self, obj):
        project_names = [project.name for project in obj.projects.filter(active=True)]

        return u"{}".format(", ".join(project_names))
    
admin.site.register(Account, AccountAdmin)
### ============== [END] ProjectTypes ============== ###

### ============== Project ============== ###
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'name', 'print_tag_names', 'created_at', 'active')

    def print_tag_names(self, obj):
        tag_names = [tag.name for tag in obj.tags.all()]

        return u"{}".format(", ".join(tag_names))

admin.site.register(Project, ProjectAdmin)
### ============== [END] Project ============== ###

### ============== UserProfile ============== ###
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('data', )

admin.site.register(UserProfile, UserProfileAdmin)
### ============== [END] UserProfile ============== ###

### ============== Data ============== ###
class DataAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'data', 'created_at')

admin.site.register(Data, DataAdmin)
### ============== [END] Data ============== ###

