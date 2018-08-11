from django.contrib import admin

from . import models


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('text', 'send_date', 'send_for_elite')
    ordering = ('send_date', )


admin.site.register(models.Announcement, AnnouncementAdmin)
admin.site.register(models.AnnouncementChronotrackTemplate)

