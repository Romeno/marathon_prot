import json
import os

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from . import models
from marathon_utils.yandex_maps import parse_geojson


class MarathonRouteAdminForm(forms.ModelForm):
    class Meta:
        fields = ['marathon', 'name', 'start_time', 'end_time', 'map', 'parsed_map',
                  'start_region_map', 'parsed_start_region_map', 'finish_region_map', 'parsed_finish_region_map',
                  'ct_race_id', 'is_active']
        widgets = {
            'parsed_map': forms.HiddenInput(),
            'parsed_start_region_map': forms.HiddenInput(),
            'parsed_finish_region_map': forms.HiddenInput()
        }
        model = models.MarathonRoute

    def full_clean(self):
        self.instance._new = self.instance.pk is None
        if not self.instance._new:
            self.instance._old_route = models.MarathonRoute.objects.get(pk=self.instance.pk)

        return super().full_clean()

    def clean_map(self):
        data = self.cleaned_data["map"]

        if not self.instance._new:
            self.instance._map_changed = data != str(self.instance._old_route.map)
        else:
            self.instance._map_changed = False

        # parse geoJSON if new or map field was changed
        if self.instance._new or self.instance._map_changed:
            full_path = os.path.join(settings.MEDIA_ROOT, self.base_fields["map"].directory, data)
            with open(full_path) as f:
                try:
                    parsed = parse_geojson(f)
                    self.cleaned_data["_parsed_map"] = parsed
                except:
                    raise ValidationError(_('Error while parsing map GeoJSON of a route map. Make sure all values are set according to agreement or contact system administrator.'))

        return data

    def clean_start_region_map(self):
        data = self.cleaned_data["start_region_map"]

        if not self.instance._new:
            self.instance._start_region_map_changed = data != str(self.instance._old_route.start_region_map)
        else:
            self.instance._start_region_map_changed = False

        # parse geoJSON if new or map field was changed
        if self.instance._new or self.instance._start_region_map_changed:
            full_path = os.path.join(settings.MEDIA_ROOT, self.base_fields["start_region_map"].directory, data)
            with open(full_path) as f:
                try:
                    parsed = parse_geojson(f)
                    self.cleaned_data["_parsed_start_region_map"] = parsed
                except:
                    raise ValidationError(_('Error while parsing map GeoJSON of a start region map. Make sure all values are set according to agreement or contact system administrator.'))

        return data

    def clean_finish_region_map(self):
        data = self.cleaned_data["finish_region_map"]

        if not self.instance._new:
            self.instance._finish_region_map_changed = data != str(self.instance._old_route.finish_region_map)
        else:
            self.instance._finish_region_map_changed = False

        # parse geoJSON if new or map field was changed
        if self.instance._new or self.instance._finish_region_map_changed:
            full_path = os.path.join(settings.MEDIA_ROOT, self.base_fields["finish_region_map"].directory, data)
            with open(full_path) as f:
                try:
                    parsed = parse_geojson(f)
                    self.cleaned_data["_parsed_finish_region_map"] = parsed
                except:
                    raise ValidationError(_('Error while parsing map GeoJSON of a finish region map. Make sure all values are set according to agreement or contact system administrator.'))

        return data

    def save(self, **kwargs):
        if self.is_valid():
            if self.instance._map_changed or self.instance._new:
                self.instance.parsed_map = str(self.cleaned_data["_parsed_map"])

            if self.instance._start_region_map_changed or self.instance._new:
                self.instance.parsed_start_region_map = self.cleaned_data["_parsed_start_region_map"]

            if self.instance._finish_region_map_changed or self.instance._new:
                self.instance.parsed_finish_region_map = self.cleaned_data["_parsed_finish_region_map"]

            return super().save(**kwargs)
