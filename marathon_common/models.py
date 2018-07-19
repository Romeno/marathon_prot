from django.db import models
from django.utils.translation import gettext_lazy as _


class Marathon(models.Model):
    class Meta:
        db_table = 'marathon'

    name = models.CharField(max_length=250, verbose_name=_("Title of a marathon"))
    time_start = models.DateTimeField(blank=True, null=True, verbose_name=_("Time when all marathon activities start"))
    time_end = models.DateTimeField(blank=True, null=True, verbose_name=_("Time when all marathon activities end"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))


class MarathonRoute(models.Model):
    class Meta:
        db_table = 'marathon_route'

    name = models.CharField(max_length=500, verbose_name=_("Route title"))
    map_url = models.CharField(max_length=2083, verbose_name=_("Url of a map created using Yandex Maps constructor"))

    is_active = models.BooleanField(verbose_name=_("Is active?"))

