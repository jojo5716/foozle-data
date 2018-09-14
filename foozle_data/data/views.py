# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

def track_data(request):
    return JsonResponse({
        "success": True
    })
