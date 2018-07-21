from django.shortcuts import render
from django.http import JsonResponse

from .models import MarathonRunner


def get_runners(req):
    from marathon_utils.random_utils import random_datetime
    import random

    runners = MarathonRunner.objects.all()
    runners_json = {
        "runners": [{
                "runnerId": r.pk,
                "runnerNumber": r.runner_number,
                "runnerName": r.first_name + " " + r.last_name,
                "distance": 0,
                "time": int(random_datetime().timestamp()),
                "isAcceleration": random.choice([True, False]),
                "citizenship": r.citizenship,
                "place": random.randint(1, 100),
            } for r in runners]
    }

    return JsonResponse(runners_json)


def get_info(req):
    pass


def add_medical_help_info(req):
    pass



