import math

import googlemaps as gm

from django.conf import settings


def get_distance_between_points(p1, p2):
    """
    Gets distance between points on Earth
    From: https://stackoverflow.com/questions/1502590/calculate-distance-between-two-points-in-google-maps-v3
    :param p1: coordinates - list [lat, long]
    :param p2: coordinates - list [lat, long]
    :return: distance in meters
    """
    r = 6378137 # Earth radius
    dLat = math.radians(p2[0] - p1[0])
    dLong = math.radians(p2[1] - p1[1])
    a = math.sin(dLat / 2) ** 2 + math.cos(math.radians(p1[0])) * math.cos(math.radians(p2[0])) * math.sin(dLong / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c
    return d


def get_route_elevation(route):
    """
    Get elevation data for a route
    :param route: list of coordinates. coordinates in YM format - [long, lat]
    :return: list of elevation data
    """
    if not route:
        return []

    gmaps = gm.Client(key='AIzaSyCo5Sy_e4yy2QHMmieUEdiYYBjmwAxixUw')

    elevation = []
    p1 = route[0][::-1]
    first = True
    for p2 in route[1:]:
        p2 = p2[::-1]
        d = get_distance_between_points(p1, p2)

        e = gmaps.elevation_along_path([p1, p2], math.ceil(d / 1000) + 1)
        if first:
            elevation.extend(e)
        else:
            elevation.extend(e[1:])
        p1 = p2
        first = False

    return elevation




if __name__ == "__main__":
    elevation = get_route_elevation([
               [
                  27.548368992953804,
                  53.910286897846916
               ],
               [
                  27.556257525191764,
                  53.902616775882464
               ],
               [
                  27.564046660171,
                  53.90610131005885
               ],
               [
                  27.561300078139755,
                  53.90805252164754
               ],
               [
                  27.55777565549415,
                  53.9092244715941
               ],
               [
                  27.55689589093726,
                  53.909553878605976
               ],
               [
                  27.556144872413107,
                  53.911289557057465
               ],
               [
                  27.553419748053965,
                  53.91406395822884
               ],
               [
                  27.552861848578864,
                  53.91522940485771
               ],
               [
                  27.553012052283705,
                  53.91782620644288
               ],
               [
                  27.545909562812252,
                  53.917281524923375
               ],
               [
                  27.539429345832293,
                  53.91439332689311
               ],
               [
                  27.545609155402598,
                  53.91244241290517
               ],
               [
                  27.548342326388777,
                  53.91030612039511
               ]
            ])

    print(elevation)