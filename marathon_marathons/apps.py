from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MarathonMarathonsConfig(AppConfig):
    name = 'marathon_marathons'
    verbose_name = _('Marathons and routes')

    def ready(self):
        from . import signals