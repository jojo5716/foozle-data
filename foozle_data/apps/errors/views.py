# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from pprint import pprint 

from ...services import errors as error_service


def track_error(request):
    body_json = json.loads(request.body)

    pprint(body_json)
    
    if body_json:
        error = error_service.update_or_create({
            "file_error": body_json.get("file", 'no file'),
            "message": body_json["message"]
        })

        error_detail = error_service.create_error_detail(body_json)

        error.errors.add(error_detail)

        for console in body_json["console"]:
            console_obj = error_service.create_console_log(console)

            error_detail.consoles.add(console_obj)
        
        for network in body_json["network"]:
            network_obj = error_service.create_network_log(network)

            error_detail.networks.add(network_obj)

    return JsonResponse({
        "success": True
    })