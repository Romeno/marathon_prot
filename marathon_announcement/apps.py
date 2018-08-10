from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MarathonAnnouncementConfig(AppConfig):
    name = 'marathon_announcement'
    verbose_name = _('Marathon Announcements')
