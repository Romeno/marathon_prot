# -*- coding: utf-8
import ast

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from . import models
from marathon_utils.yandex_maps import parse_geojson
from marathon_utils.google_maps import get_route_elevation
from marathon_utils.exceptions import DoesNotExistException


def get_route_map(req, id):
    try:
        route = models.MarathonRoute.objects.get(pk=id)
    except models.MarathonRoute.DoesNotExist as e:
        raise DoesNotExistException("route id={}".format(id))

    parsed = ast.literal_eval(route.parsed_map)

    return JsonResponse(parsed)


def get_route_heights(req, id):
    try:
        route = models.MarathonRoute.objects.get(pk=id)
    except models.MarathonRoute.DoesNotExist as e:
        raise DoesNotExistException("route id={}".format(id))

    elevation = ast.literal_eval(route.raw_elevation_data)

    return JsonResponse(elevation)


def get_start_region_map(req, id):
    try:
        route = models.MarathonRoute.objects.get(pk=id)
    except models.MarathonRoute.DoesNotExist as e:
        raise DoesNotExistException("route id={}".format(id))

    parsed = ast.literal_eval(route.parsed_start_region_map)

    return JsonResponse(parsed)


def get_finish_region_map(req, id):
    try:
        route = models.MarathonRoute.objects.get(pk=id)
    except models.MarathonRoute.DoesNotExist as e:
        raise DoesNotExistException("route id={}".format(id))

    parsed = ast.literal_eval(route.parsed_finish_region_map)

    return JsonResponse(parsed)
