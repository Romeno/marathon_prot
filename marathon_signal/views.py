from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from django.contrib.auth.models import User

from . import models


def signal_medical_incident(req):
	res = {}

	try:
		coords = req.POST.get('coords')
		initiator = User.objects.filter(pk=req.POST.get('user_id'))
		ambulance = req.POST.get('ambulance')
		severity = req.POST.get('severity')
		mi = models.MedicalIncident(coords=coords, initiator=initiator, ambulance_required=ambulance,
							   severity=severity)
		mi.save()

		res['result'] = 'ok'
	except Exception as e:
		res['result'] = 'error'

	return JsonResponse(res)


def signal_danger(req):
	res = {}

	try:
		coords = req.POST.get('coords')
		initiator = User.objects.filter(pk=req.POST.get('user_id'))
		ambulance = req.POST.get('ambulance')
		severity = req.POST.get('severity')
		type = req.POST.get('type')
		mi = models.DangerIncident(coords=coords, initiator=initiator, ambulance_required=ambulance,
								   severity=severity, type=type)
		mi.save()

		res['result'] = 'ok'
	except Exception as e:
		res['result'] = 'error'

	return JsonResponse(res)


def get_signals(req):
	signals = models.SignalBase.objects.all()

	return JsonResponse(signals)


def get_danger_types(req):
	dt = models.DangerType.objects.all()

	return JsonResponse(dt)


def get_incident_severities(req):
	inc_sev = models.IncidentSeverity.objects.all()

	return JsonResponse(inc_sev)


def get_danger_severities(req):
	ds = models.DangerSeverity.objects.all()

	return JsonResponse(ds)

