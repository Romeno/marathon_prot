from django.shortcuts import render
from django.http import JsonResponse

from . import models


def get_expo_info(req):
    map = models.ExpoMap.objects.all().first()
    stands = models.ExpoStand.objects.all()

    expo = {
        "map": map.image.url,
        "stands": [
        ]
    }

    for stand in stands:
        expo["stands"].append({
            "name": stand.name,
            "website": stand.website,
            "description": stand.text,
            "categories": [],
            "top_left": [stand.top_left_x, stand.top_left_y],
            "size": [stand.width, stand.height],
        })

    return JsonResponse(expo)