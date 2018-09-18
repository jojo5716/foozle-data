# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import HStoreField


class ConsoleError(models.Model):
    type_console = models.CharField(u"Console log type", max_length=100)
    message = models.TextField(u"Message", blank=True, null=True)
    timeStamp = models.DateTimeField()
    
class Network(models.Model):
    startedOn = models.DateTimeField()
    completedOn = models.DateTimeField()
    url = models.TextField()
    method = models.CharField(u"Method", max_length=100)
    status = models.CharField(u"Status", max_length=100)
    

class ErrorDetail(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    type_name = models.CharField(u"Error type", max_length=100, default="window")
    line = models.IntegerField(blank=True, null=True)
    consoles = models.ManyToManyField(ConsoleError, blank=True)
    networks = models.ManyToManyField(Network, blank=True)
    url = models.TextField(blank=True, null=True)
    foozle_version = models.CharField(u"Foozle version", max_length=100)
    meta_data = HStoreField(default=dict, blank=True)

    def __unicode__(self):
        return u"{}".format(self.url)
        
class Error(models.Model):
    file_error = models.TextField(u"File", blank=True, null=True)
    message = models.TextField(u"Message", blank=True, null=True)
    issues = models.IntegerField(blank=True, null=True, default=1)
    errors = models.ManyToManyField(ErrorDetail)