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


def get_route(req, id):
    return JsonResponse({})