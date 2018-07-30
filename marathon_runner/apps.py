from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MarathonRunnerConfig(AppConfig):
    name = 'marathon_runner'
    verbose_name = _('Marathon runners')