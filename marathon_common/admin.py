from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# from flatblocks.models import FlatBlock
# from flatblocks.forms import FlatBlockForm
from tinymce.widgets import TinyMCE

from . import models


# class FlatBlockForm2(FlatBlockForm):
#     class Meta:
#         widgets = {
#             'content': TinyMCE(attrs={'cols': 80, 'rows': 30})
#         }
#
#
# class FlatBlockAdmin(admin.ModelAdmin):
#     ordering = ['slug', ]
#     list_display = ('slug', 'header')
#     search_fields = ('slug', 'header', 'content')
#     form = FlatBlockForm2

# class FlatBlockAdmin(admin.ModelAdmin):
#     ordering = ['slug', ]
#     list_display = ('slug', 'header')
#     search_fields = ('slug', 'header', 'content')

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

admin.site.register(models.PhotoFrame)
#
# admin.site.unregister(FlatBlock)
# admin.site.register(FlatBlock, FlatBlockAdmin)
admin.site.register(models.MenuItem, MenuItemAdmin)
admin.site.register(models.MenuItemGroup, MenuItemGroupAdmin)

# title shown on index admin page
admin.site.index_title = _('MCS Administrator control panel')

# hides view site button in admin
admin.site.site_url = None
