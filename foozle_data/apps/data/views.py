# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import JsonResponse
from django.shortcuts import render


def track_data(request):
    body_json = json.loads(request.body)

    print "=" * 90
    from pprint import pprint
    pprint(body_json)

    if request.method == "POST":
        return JsonResponse({
            "success": True
        })
