from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError

from filebrowser.fields import FileBrowseField
from tinymce.models import HTMLField

from marathon_marathons.models import MarathonRoute


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


class MenuItemGroup(models.Model):
    class Meta:
        db_table = 'marathon_menu_item_group'
        verbose_name = _('Menu item group')
        verbose_name_plural = _('Menu item groups')

    route = models.ForeignKey(MarathonRoute, on_delete=models.CASCADE, verbose_name=_("Route for which menu content is set"))
    title = models.CharField(max_length=256, verbose_name=_("Menu item group title"))

    def __str__(self):
        return "{} ({})".format(self.title, self.route.name)


class MenuItem(models.Model):
    class Meta:
        db_table = 'marathon_menu_item'
        verbose_name = _('Menu item')
        verbose_name_plural = _('Menu items')

    route = models.ForeignKey(MarathonRoute, on_delete=models.CASCADE, verbose_name=_("Route for which menu content is set"))
    group = models.ForeignKey(MenuItemGroup, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Menu item group"))
    name = models.CharField(max_length=256, verbose_name=_("Menu item name used in server code"), help_text=_("Cannot be edited"))
    title = models.CharField(max_length=256, verbose_name=_("Menu item title text"), help_text=_("You can dynamically change menu of the mobile app from here. Changing title of a menu item will change the menu item title in the hamburger menu."))
    text = HTMLField(verbose_name=_("Contents of a page shown when user clicks menu item"))

    def __str__(self):
        return self.title

    def full_clean(self, exclude=None, validate_unique=True, **kwargs):
        if self.group and self.route.pk != self.group.route.pk:
            raise ValidationError(_('Route of the group is not the same as route of the menu item'))

        return super().full_clean()

