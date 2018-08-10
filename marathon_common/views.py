# -*- coding: utf-8
import ast

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from . import models
from marathon_marathons.models import Marathon, MarathonRoute
from marathon_utils.exceptions import DoesNotExistException


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


def get_route_info(req, id):
    top_level_menu = models.MenuItemGroup.objects.all()

    info = {
        "menu": []
    }

    for top_level_item in top_level_menu:
        top_level_item_dict = {
            "ru": top_level_item.title,
            "menu_items": [
            ]
        }

        menu_items = top_level_item.menuitem_set.objects.all()
        for menu_item in menu_items:
            top_level_item_dict["menu_items"].append({
                # "en": menu_item.name,
                "ru": menu_item.title,
                "text": menu_item.text,
            })

        info["menu"].append(top_level_item_dict)

    menu_items_no_top_level = models.MenuItem.objects.filter(group=None)
    for mintl in menu_items_no_top_level:
        info["menu"].append({
            # "en": mintl.name,
            "ru": mintl.title,
            "text": mintl.text,
        })

    return JsonResponse(info)


def get_photo_frames(req):
    photos = models.PhotoFrame.objects.filter(is_active=True)
    body = [{
        "id": p.pk,
        "image": p.image.url
    } for p in photos]

    resp = {
        "photo_frames": body
    }

    return JsonResponse(resp)

