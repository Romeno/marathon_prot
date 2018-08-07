from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField


class Marathon(models.Model):
    class Meta:
        db_table = 'marathon'
        verbose_name = _('Marathon')
        verbose_name_plural = _('Marathons')

    name = models.CharField(max_length=1024, verbose_name=_("Title of a marathon"))
    start_time = models.DateTimeField(verbose_name=_("Time when all marathon activities start"))
    end_time = models.DateTimeField(verbose_name=_("Time when all marathon activities end"))
    ct_event_id = models.IntegerField(verbose_name=_("Chronotrack event Id for this marathon"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return self.name


class MarathonRoute(models.Model):
    class Meta:
        db_table = 'marathon_route'
        verbose_name = _('Marathon route')
        verbose_name_plural = _('Marathon routes')

    marathon = models.ForeignKey(Marathon, on_delete=models.CASCADE, verbose_name=_("Marathon whose route it is"))

    name = models.CharField(max_length=1044, verbose_name=_("Route title")) # Растояния в км( число с запятой) {км} {Наименование забега}
    start_time = models.DateTimeField(blank=True, null=True, verbose_name=_("Time when all marathon activities start"))
    end_time = models.DateTimeField(blank=True, null=True, verbose_name=_("Time when all marathon activities end"))
    # map_url = models.CharField(max_length=2083, verbose_name=_("Url of a map created using Yandex Maps constructor"))

    map = FileBrowseField(max_length=2048, extensions=settings.FILEBROWSER_EXTENSIONS['GeoJSON'], format='GeoJSON', verbose_name=_("GeoJSON of exported Yandex Constructor map of the route"))
    parsed_map = models.TextField(blank=True)
    raw_elevation_data = models.TextField(blank=True)

    start_region_map = FileBrowseField(max_length=2048, extensions=settings.FILEBROWSER_EXTENSIONS['GeoJSON'], format='GeoJSON', verbose_name=_("GeoJSON of exported Yandex Constructor map of the start region"))
    parsed_start_region_map = models.TextField(blank=True)

    finish_region_map = FileBrowseField(max_length=2048, extensions=settings.FILEBROWSER_EXTENSIONS['GeoJSON'], format='GeoJSON', verbose_name=_("GeoJSON of exported Yandex Constructor map of the finish region"))
    parsed_finish_region_map = models.TextField(blank=True)

    ct_race_id = models.IntegerField(verbose_name=_("Chronotrack race Id for this marathon route"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return self.name


class MarathonHeight(models.Model):
    class Meta:
        db_table = 'marathon_height'
        verbose_name = _('Marathon route heights')
        verbose_name_plural = _('Marathon routes heigths')

    route = models.ForeignKey(MarathonRoute, on_delete=models.CASCADE, verbose_name=_("Route for which heights are specified"))
    lat = models.FloatField(verbose_name=_("Latitude of the point on the route"))
    long = models.FloatField(verbose_name=_("longitude of the point on the route"))
    elevation = models.FloatField(verbose_name=_("Elevation of the point in meters"))
    resolution = models.FloatField(verbose_name=_("Resolution of the point elevation in meters"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return "{:.4f} {:.4f} {:.0f}".format(self.lat, self.long, self.elevation)