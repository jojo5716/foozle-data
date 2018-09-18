# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import datetime

from django.http import JsonResponse
from django.shortcuts import render

from ...services import (
    project as project_service,
    user as user_service,
    navigation as navigation_service,
    page as page_service,
    bookings as bookings_service,
    availabilities as availability_service,
    action as action_service
)

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
    def register_array_field(instance, field_name, value):
        if value:
            values = getattr(instance, field_name, [])
            values.append(value)

    if request.method == "POST":
        body_json = json.loads(request.body)
        project = project_service.get_project_by_uuid(body_json["project"])

        if project:
            # Getting user visitor profile
            pprint(body_json)
            user_session = body_json["data"]["session"]
            user, user_created = user_service.get_or_create(user_session)

            # Generating a new page, if this page it's same that the before,
            # is beacause user reload the page.
            page = page_service.create_page(body_json["data"])
     
            booking = bookings_service.create_or_update(body_json["data"]["booking"])

            availability = availability_service.create(body_json["data"])
            
            # Try to get the navigation or create one if does not exist (first request for the user)
            navigation_query = {
                "user": user,
                "project": project,
                "session_id": body_json["data"]["sessionTemp"],
                "user_info": body_json["data"]["userInfo"],
            }

            navigation, navCreated = navigation_service.get_or_create(navigation_query, page)

            navigation.pages.add(page)
            if booking:
                navigation.bookings.add(booking)
            
            if availability:
                navigation.availabilities.add(availability)

            navigation.last_view = datetime.datetime.now()

        return JsonResponse({
            "success": True
        })


def track_action(request):
    body_json = json.loads(request.body)
    pprint(body_json)
    page_token = body_json["data"]["pageToken"]
    action_data = body_json["data"].get("actions")

    if isinstance(body_json, dict) and page_token and action_data:
        page = page_service.get_by_id(page_token)

        if page:
            action_data = body_json["data"]["actions"]

            action = action_service.create(action_data, page) if action_data else None


    return JsonResponse({
        "success": True
    })