from django.shortcuts import render
from django.http import JsonResponse

from .models import Marathon, MarathonRoute


def get_settings(req):
    current_marathon = Marathon.objects.filter(is_active=True).order_by("start_time").first()
    routes = MarathonRoute.objects.filter(is_active=True).order_by("start_time")

    settings = {
        "marathon": {
            "id": current_marathon.pk,
            "name": current_marathon.name,
            "start_time": current_marathon.start_time.timestamp(),
            "end_time": current_marathon.end_time.timestamp(),
            "marathon_routes": [
            ]
        },
    }

    for r in routes:
        route = {
            "route_id": r.pk,
            "name": r.name,
            "start_time": r.start_time.timestamp(),
            "end_time": r.end_time.timestamp(),
        }

        settings["marathon"]["marathon_routes"].append(route)

    return JsonResponse(settings)


def get_route_map(req, id):
    return JsonResponse({})


def get_route_heights(req, id):
    return JsonResponse({})


def get_route_info(req, id):
    info = {
        "schedule": "<b>lorem ipsum</b>",
        "awards": "<b>lorem ipsum</b>",
        "register": "<b>lorem ipsum</b>",
        "terms": "<b>lorem ipsum</b>",
        "costs": "<b>lorem ipsum</b>",
        "qualification": "<b>lorem ipsum</b>",
        "number": "<b>lorem ipsum</b>",
        "runner_packet_what": "<b>lorem ipsum</b>",
        "runner_packet_how": "<b>lorem ipsum</b>",
        "medical_certificate": "<b>lorem ipsum</b>",
        "start": "<b>lorem ipsum</b>",
        "finish": "<b>lorem ipsum</b>",
        "pacemakers": "<b>lorem ipsum</b>",
        "medical_help": "<b>lorem ipsum</b>",
        "hotels": "<b>lorem ipsum</b>",
        "for_fans": "<b>lorem ipsum</b>",
        "volunteers": "<b>lorem ipsum</b>",
    }

    return JsonResponse(info)


def get_expo_info(req):
    expo = {
        "map": "http://server/someimg.png",
        "stands": [
            {
                "name": "Coca-cola",
                "website": "http://coca-cola.com",
                "description": "<b>lorem ipsum</b>",
                "categories": ["еда",],
                "topLeft": [0,0],
                "size": [100, 100],
            },
            {
                "name": "Nike",
                "website": "http://nike.com",
                "description": "<b>lorem ipsum</b>",
                "categories": ["экипировка", "одежда"],
                "topLeft": [550, 30],
                "size": [200, 20],
            },
        ]
    }

    return JsonResponse(expo)


def get_start_region_map(req):
    return JsonResponse({})


def get_finish_region_map(req):
    return JsonResponse({})


def get_photo_frames(req):
    return JsonResponse({})

