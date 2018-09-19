# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import datetime

from django.db import transaction

from celery.decorators import task

from ...services import errors as error_service
from ...helpers.slack import notify_error


@task(name="saving_error")
@transaction.atomic
def register_error(body_json):
    if body_json:
        error = error_service.update_or_create({
            "file_error": body_json.get("file", ''),
            "message": body_json.get("message", '')
        })

        error_detail = error_service.create_error_detail(body_json)

        error.errors.add(error_detail)

        for console in body_json["console"]:
            console_obj = error_service.create_console_log(console)

            error_detail.consoles.add(console_obj)
        
        for network in body_json["network"]:
            network_obj = error_service.create_network_log(network)

            error_detail.networks.add(network_obj)
        
        # if any error has file from being exeption, its because the error
        # its ours.
        if error.file_error:
            notify_error(error)