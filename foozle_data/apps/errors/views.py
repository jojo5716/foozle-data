# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse

from .workers import register_error


def track_error(request):
    body_json = json.loads(request.body)

    if body_json:
       register_error.delay(body_json)

    return JsonResponse({
        "success": True
    })