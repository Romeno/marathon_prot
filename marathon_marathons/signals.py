import ast

from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models
from marathon_utils.google_maps import get_route_elevation


@receiver(post_save, sender=models.MarathonRoute)
def save_route_heights(sender, **kwargs):
    route = kwargs["instance"]
    created = kwargs["created"]

    if route._map_changed:
        heights = models.MarathonHeight.objects.filter(route=route)
        for h in heights:
            h.delete()

    if route._map_changed or created:
        parsed_map = ast.literal_eval(route.parsed_map)

        elevation = get_route_elevation(parsed_map["route"])
        for p in elevation:
            mh = models.MarathonHeight.objects.create(route=route,
                                               lat=p["location"]["lat"],
                                               long=p["location"]["lng"],
                                               elevation=p["elevation"],
                                               resolution=p["resolution"])

        models.MarathonRoute.objects.filter(pk=route.pk).update(raw_elevation_data=str({"points": elevation}))



