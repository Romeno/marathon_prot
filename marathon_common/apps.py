from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MarathonCommonConfig(AppConfig):
    name = 'marathon_common'
    verbose_name = _('Other entities')


class FlatblocksAppConfig(AppConfig):
    name = 'flatblocks'
    verbose_name = _("Mobile App and MCS texts")
