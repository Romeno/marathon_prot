from django.shortcuts import render
from .models import Medic
from django.http import JsonResponse


def get_medics_info(req):
    m = Medic.objects.all()

    return JsonResponse({})

