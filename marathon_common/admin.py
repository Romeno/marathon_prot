from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


class MenuItemGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'route')
    ordering = ('route', 'pk')


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'route')
    ordering = ('route', 'group', 'pk')

    def get_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['route', 'group', 'title', 'text']

        return ['route', 'group', 'name', 'title', 'text']


class MapObjectIconAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['object_type']

        return []

    def get_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['object_type', 'image']

        return ['object_type_key', 'object_type', 'image']


admin.site.register(models.PhotoFrame)

admin.site.register(models.MenuItem, MenuItemAdmin)
admin.site.register(models.MenuItemGroup, MenuItemGroupAdmin)

admin.site.register(models.MapObjectIcon, MapObjectIconAdmin)

# title shown on index admin page
admin.site.index_title = _('MCS Administrator control panel')

# hides view site button in admin
admin.site.site_url = None
