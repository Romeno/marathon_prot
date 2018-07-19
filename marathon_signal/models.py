from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils.timezone import now


# class DangerType(models.Model):
#     name = models.CharField(max_length=100, verbose_name=_("Danger type"))
#
#
# class IncidentSeverity(models.Model):
#     name = models.CharField(max_length=100, verbose_name=_("Incident severity"),
#                             help_text=_("How is the incident severe"))
#
#
# class MedicalSeverity(IncidentSeverity):
#     pass
#
#
# class DangerSeverity(IncidentSeverity):
#     pass
#
#
# class SignalBase(models.Model):
#     NEW = 'new'
#     IN_PROGRESS = 'wip'
#     RESOLVED = 'res'
#     SIGNAL_STATUS = (
#         (NEW, _('New')),
#         (IN_PROGRESS, _('In progress')),
#         (RESOLVED, _('Resolved')),
#     )
#
#     date = models.DateTimeField(blank=False, default=now,
#                                 verbose_name=_("Time happened"), help_text=_("When happened"))
#     coords = models.CharField(max_length=20, blank=False,
#                               verbose_name=_("Signal coordinates"), help_text=_("Where happened"))
#     initiator = models.ForeignKey(to=User, blank=False, on_delete=models.CASCADE,
#                                   verbose_name=_("Member initiator"), help_text=_("From whom"))
#     description = models.TextField(blank=True,
#                                    verbose_name=_("Incident description"), help_text=_("What happened"))
#     ambulance_required = models.BooleanField(blank= True,
#                                              verbose_name=_("Ambulance requirement"), help_text=_("Is ambulance required"))
#     status = models.CharField(choices=SIGNAL_STATUS, max_length=3, blank=False, default=NEW,
#                               verbose_name=_("Signal status"), help_text=_("signal status"))
#
#
# class MedicalIncident(SignalBase):
#     severity = models.ForeignKey(to=MedicalSeverity, blank=False, on_delete=models.CASCADE,
#                                  verbose_name=_("Incident severity"), help_text=_("How much the incident is severe"))
#
#
# class DangerIncident(SignalBase):
#     severity = models.ForeignKey(to=DangerSeverity, blank=False, on_delete=models.CASCADE,
#                                  verbose_name=_("Incident severity"), help_text=_("How much the incident is severe"))
#     type = models.ForeignKey(to=DangerType, blank=False, on_delete=models.CASCADE,
#                              verbose_name=_("Incident type"))


