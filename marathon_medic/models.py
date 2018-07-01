from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Medic(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	coords = models.CharField(max_length=20, blank=False,
							  verbose_name=_("Person coordinates"), help_text=_("GPS coordinates"))


class MedicManager(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

