from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from filebrowser.fields import FileBrowseField
from tinymce.models import HTMLField

from marathon_utils.django import validate_only_one_instance


class ExpoStand(models.Model):
    class Meta:
        db_table = 'marathon_expo_stand'
        verbose_name = _('Expo stand')
        verbose_name_plural = _('Expo stands')

    name = models.CharField(max_length=100, verbose_name=_("Stand name"))
    website = models.URLField(verbose_name=_("Website"))
    text = HTMLField(verbose_name=_("Stand description, special offers, etc"))

    top_left_x = models.IntegerField(verbose_name=_("X of top left corner of expo stand on the map image"))
    top_left_y = models.IntegerField(verbose_name=_("Y of top left corner of expo stand on the map image"))
    width = models.IntegerField(verbose_name=_("Width of the expo stand on the map image"))
    height = models.IntegerField(verbose_name=_("Height of the expo stand on the map image"))

    def __str__(self):
        return self.name


class ExpoMap(models.Model):
    class Meta:
        db_table = 'marathon_expo_map'
        verbose_name = _('Expo map')
        verbose_name_plural = _('Expo maps')

    image = FileBrowseField(max_length=2048, extensions=settings.FILEBROWSER_EXTENSIONS['Image'], format='Image', verbose_name=_("Photo frame image"))

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return str(ExpoMap._meta.verbose_name)

