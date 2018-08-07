from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from filebrowser.fields import FileBrowseField


class PhotoFrame(models.Model):
    class Meta:
        db_table = 'marathon_photo_frame'
        verbose_name = _('Photo frame')
        verbose_name_plural = _('Photo frames')

    image = FileBrowseField(max_length=2048, extensions=settings.FILEBROWSER_EXTENSIONS['Image'], format='Image', verbose_name=_("Photo frame image"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def __str__(self):
        return _('%(model_name)s #%(id)d') % {
            'model_name': PhotoFrame._meta.verbose_name,
            'id': self.pk
        }


class Announcement(models.Model):
    class Meta:
        db_table = 'marathon_announcement'
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')

    text = models.TextField(verbose_name=_("Announcement text"))
    send_date = models.DateTimeField(verbose_name=_("Announcement date and time"),
                                     help_text=_("Announcement send date and time should be later than the current date and time"))
    send_for_elite = models.BooleanField(verbose_name=_("Send only to elite participants"))

    def __str__(self):
        return "{}...".format(self.text[:50])


class ExpoStand(models.Model):
    class Meta:
        db_table = 'marathon_expo_stand'
        verbose_name = _('Expo stand')
        verbose_name_plural = _('Expo stands')

    name = models.CharField(max_length=100, verbose_name=_("Stand name"))
    text = models.TextField(verbose_name=_("Announcement text"))

    top_left_x = models.IntegerField(verbose_name=_("X of top left corner of expo stand on the map image"))
    top_left_y = models.IntegerField(verbose_name=_("Y of top left corner of expo stand on the map image"))
    width = models.IntegerField(verbose_name=_("Width of the expo stand on the map image"))
    height = models.IntegerField(verbose_name=_("Height of the expo stand on the map image"))

    def __str__(self):
        return self.name
