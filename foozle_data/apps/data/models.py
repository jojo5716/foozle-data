# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.postgres.fields import HStoreField, ArrayField
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
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{}".format(self.name)

class Account(models.Model):
    name = models.CharField("Nombre de la cuenta", max_length=200)
    projects = models.ManyToManyField(Project)

    def __unicode__(self):
        return u"{}".format(self.name)


class UserProfile(models.Model):
    data = HStoreField(default=dict, blank=True)
    unique_id = models.CharField(max_length=200)

    def __unicode__(self):
        return u"{}".format(self.unique_id)
    

class Data(models.Model):
    project = models.OneToOneField(Project)
    user = models.OneToOneField(UserProfile, related_name="user")
    data = HStoreField(default=dict, blank=True)
    meta_data = HStoreField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Page(models.Model):
    unique_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    data = HStoreField(default=dict, blank=True)
    meta_data = HStoreField(default=dict, blank=True)
    enviroment = HStoreField(default=dict, blank=True)

    def __unicode__(self):
        return u"{}".format(self.data.get("url", '---'))
    
class Action(models.Model):
    page = models.ForeignKey(Page)
    action = HStoreField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        action_names = self.action.keys()

        return u"{}".format(action_names[0] if action_names else "Unknown action")

class Booking(models.Model):
    code = models.CharField(max_length=200)
    data = HStoreField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Availability(models.Model):
    hotel = HStoreField(default=dict, blank=True)
    data = HStoreField(default=dict, blank=True)


class Navigation(models.Model):
    user = models.OneToOneField(UserProfile)
    project = models.OneToOneField(Project)
    session_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_view = models.DateTimeField(auto_now=True)
    pages = models.ManyToManyField(Page, blank=True)
    bookings = models.ManyToManyField(Booking, blank=True, null=True)
    availabilities = models.ManyToManyField(Availability, blank=True, null=True)
    user_info = HStoreField(default=dict, blank=True)


