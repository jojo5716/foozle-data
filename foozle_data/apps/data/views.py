# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import JsonResponse

from ...services import (
    project as project_service,
    page as page_service,
    action as action_service
)

from .workers import register_data, register_action

from pprint import pprint


def track_data(request):
    """
    Track all data sended by a onLoad request

    Here we can save an initial structure of data.

    Ejem:
        {u'data': {u'actions': {},
                u'availability': {},
                u'booking': {},
                u'enviroment': {u'userAgent': u'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 ...',
                                u'viewportHeight': 812,
                                u'viewportWidth': 375},
                u'eventTime': 1537032589797,
                u'loadedOn': 1537032589797,
                u'metaData': {u'channel': u'webmobile', u'language': u'en'},
                u'page': {u'previousURL': u'',
                            u'url': u'https://www.bhmallorca.com/m2/'},
                u'pageToken': u'c54cd929-3fe7-4704-a961-c7ff35f03532',
                u'session': u'b2625c38-c587-4f01-813a-dd6eaceb165d',
                u'sessionTemp': u'2b639fb0-fghy7-11e8-8307-sfj3488f0908947-8978629234nh7',
                u'userInfo': {u'country': u'',
                                u'ip': u'127.0.0.1',
                                u'latitude': u'',
                                u'longitude': u'',
                                u'zip': u'127.0.0.1'}},
        u'project': u'09da745a-6df1-9326-445a-bbc659b97642e'}

    """
    if request.method == "POST":
        body_json = json.loads(request.body)
        project = project_service.get_project_by_uuid(body_json["project"])
       
        if project:
            register_data.delay(body_json)

    return JsonResponse({
        "success": True
    })


def track_action(request):
    body_json = json.loads(request.body)

    register_action.delay(body_json)

    return JsonResponse({
        "success": True
    })
