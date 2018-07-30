from django.db import models
from django.utils.translation import gettext_lazy as _


class Marathon(models.Model):
    class Meta:
        db_table = 'marathon'
        verbose_name = _('Marathon')
        verbose_name_plural = _('Marathons')

    name = models.CharField(max_length=1024, verbose_name=_("Title of a marathon"))
    start_time = models.DateTimeField(verbose_name=_("Time when all marathon activities start"))
    end_time = models.DateTimeField(verbose_name=_("Time when all marathon activities end"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return self.name


class MarathonRoute(models.Model):
    class Meta:
        db_table = 'marathon_route'
        verbose_name = _('Marathon route')
        verbose_name_plural = _('Marathon routes')

    name = models.CharField(max_length=1044, verbose_name=_("Route title")) # Растояния в км( число с запятой) {км} {Наименование забега}
    start_time = models.DateTimeField(blank=True, null=True, verbose_name=_("Time when all marathon activities start"))
    end_time = models.DateTimeField(blank=True, null=True, verbose_name=_("Time when all marathon activities end"))
    # map_url = models.CharField(max_length=2083, verbose_name=_("Url of a map created using Yandex Maps constructor"))

    is_active = models.BooleanField(verbose_name=_("Is active"))

    def __str__(self):
        return self.name
