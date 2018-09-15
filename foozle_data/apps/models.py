# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Configuration(models.Model):
    auto_create_project = models.BooleanField(
        default=False,
        help_text="Si se marca esta casilla, no será necesario crear los proyectos en el admin, se auto crearán "
                "dependiendo de los datos que vayan llegando")
