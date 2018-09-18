# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Error,
    ErrorDetail,
    ConsoleError,
    Network,
)


### ============== Error ============== ###
class ErrorDetailInline(admin.TabularInline):
    model = Error.errors.through
    extra = 0

class ErrorAdmin(admin.ModelAdmin):
    list_display = ('file_error', 'message', 'issues')
    filter_horizontal = ('errors', )
    inlines = [ ErrorDetailInline]
    
admin.site.register(Error, ErrorAdmin)
### ============== [END] Error ============== ###

### ============== ErrorDetail ============== ###

class ErrorDetailAdmin(admin.ModelAdmin):
    list_display = ('url', 'line', 'type_name', 'foozle_version', 'created_at')
    filter_horizontal = ('consoles', 'networks')

    
admin.site.register(ErrorDetail, ErrorDetailAdmin)
### ============== [END] ErrorDetail ============== ###


### ============== ConsoleError ============== ###

class ConsoleErrorAdmin(admin.ModelAdmin):
    list_display = ('type_console', 'message', 'timeStamp',)

    
admin.site.register(ConsoleError, ConsoleErrorAdmin)
### ============== [END] ConsoleError ============== ###

### ============== Network ============== ###

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('show_short_url', 'method', 'status', 'startedOn', 'completedOn')

    def show_short_url(self, obj):
        return u"{}...".format(obj.url[:100])
    
admin.site.register(Network, NetworkAdmin)
### ============== [END] Network ============== ###
