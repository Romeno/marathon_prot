from django.contrib import admin

from . import models
from . import forms


class MarathonRouteAdmin(admin.ModelAdmin):
    form = forms.MarathonRouteAdminForm

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['map'].validators.append(forms.validate_geojson)
    #     return form


class MarathonHeightAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'route')
    ordering = ('route', 'pk')


admin.site.register(models.Marathon)
admin.site.register(models.MarathonRoute, MarathonRouteAdmin)
admin.site.register(models.MarathonHeight, MarathonHeightAdmin)
