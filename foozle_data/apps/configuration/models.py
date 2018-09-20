# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Configuration(models.Model):
    auto_create_project = models.BooleanField(
        default=False,
        help_text="Si se marca esta casilla, no será necesario crear los proyectos en el admin, se auto crearán "
                "dependiendo de los datos que vayan llegando")
    slack_token = models.CharField("Slack token", max_length=200, blank=True, null=True)
    slack_notify = models.BooleanField(default=True)
    slack_channel = models.CharField("Slack channel to notify", max_length=100, blank=True, null=True)
