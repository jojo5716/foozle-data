# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import JsonResponse
from django.shortcuts import render

from ...services import (
    project as project_service,
    user as user_service,
    navigation as navigation_service,
    page as page_service,
    bookings as bookings_service,
    availabilities as availability_service
)

from pprint import pprint
from pprint import pprint


def track_data(request):

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
     
            booking = bookings_service.get_and_update(body_json["data"]["booking"])

            availability = availability_service.create(body_json["data"])
            
            # TODO: - Falta registrar las busquedas de disponibilidad
            #       - Relacionar los bookings y availabilities al navigation
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

        return JsonResponse({
            "success": True
        })
