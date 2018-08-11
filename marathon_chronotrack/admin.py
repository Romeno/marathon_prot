from django.contrib import admin

from . import models


class MarathonRunnerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'runner_number', 'route', 'age', 'gender', 'citizenship', 'city', 't_shirt_size')
    ordering = ('route', 'runner_number')


admin.site.register(models.CtBracket)
admin.site.register(models.CtTimingPoint)
admin.site.register(models.CtInterval)
admin.site.register(models.MarathonRunner, MarathonRunnerAdmin)
