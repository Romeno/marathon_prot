from django.db import models
from django.utils.translation import gettext_lazy as _

from tinymce.models import HTMLField

from marathon_utils.django import validate_only_one_instance


class Announcement(models.Model):
    class Meta:
        db_table = 'marathon_announcement'
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')

    text = HTMLField(verbose_name=_("Announcement text"))
    send_date = models.DateTimeField(verbose_name=_("Announcement date and time"),
                                     help_text=_("Announcement send date and time should be later than the current date and time"))
    send_for_elite = models.BooleanField(verbose_name=_("Send only to elite participants"))

    def __str__(self):
        return "{}...".format(self.text[:50])


class AnnouncementChronotrackTemplate(models.Model):
    class Meta:
        db_table = 'marathon_announcement_ct_template'
        verbose_name = _('Announcement Chronotrack template')
        verbose_name_plural = _('Announcement Chronotrack templates')

    text = HTMLField(verbose_name=_("Template text"), help_text=_("The announcement about Chronotrack events will be sent to the mobile app users using this template"))

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return self.text[:50]



