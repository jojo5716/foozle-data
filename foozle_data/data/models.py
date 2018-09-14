# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.postgres.fields import HStoreField
from django.db import models


class ProjectTypes(models.Model):
    name = models.CharField("Project type name",
    max_length=100,
    help_text="Ejem: Vacacional, Urbano, Individual, Corporativa, etc...")

    def __unicode__(self):
        return u"{}".format(self.name)


class Project(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField("Nombre del proyecto", max_length=200)
    tags = models.ManyToManyField(ProjectTypes)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{}".format(self.name)

class Account(models.Model):
    name = models.CharField("Nombre de la cuenta", max_length=200)
    projects = models.ManyToManyField(Project)

    def __unicode__(self):
        return u"{}".format(self.name)


class UserProfile(models.Model):
    data = HStoreField(default=dict, blank=True)

    def __unicode__(self):
        return u"{}".format(self.data.get("name", "anonymous"))
    

class Data(models.Model):
    project = models.OneToOneField(Project)
    user = models.OneToOneField(UserProfile, related_name="user")
    data = HStoreField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)