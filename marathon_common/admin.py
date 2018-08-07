from django.contrib import admin

from flatblocks.models import FlatBlock
from flatblocks.forms import FlatBlockForm
from tinymce.widgets import TinyMCE

from . import models


class FlatBlockForm2(FlatBlockForm):
    class Meta:
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }


class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')
    form = FlatBlockForm2


admin.site.register(models.PhotoFrame)
admin.site.register(models.Announcement)
admin.site.register(models.ExpoStand)

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, FlatBlockAdmin)
