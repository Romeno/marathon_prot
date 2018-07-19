from django.shortcuts import render
from django.http import JsonResponse


def get_runners(req):
    from marathon_utils.random import random_datetime
    import random

    runners = [
        {
            "runnerId": 0,
            "runnerNumber": 0,
            "runnerName": "",
            "distance": 0,
            "time": random_datetime(),
            "isAcceleration": random.choice([True, False]),
            "citizenship": random.choice(["BY", "RU", "UA"]),
            "point": 0,
        } for i in range(random.randint(3, 8))
    ]

    return JsonResponse(runners)


def get_info(req):
    pass


def add_medical_help_info(req):
    pass



