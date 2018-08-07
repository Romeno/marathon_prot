import json

from django import forms
from .models import MarathonRoute, MarathonHeight

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
        model = MarathonRoute

    def clean_map(self):
        # do something that validates your data
        return self.cleaned_data["map"]

    def save(self, **kwargs):
        if self.is_valid():
            new = False
            self.instance.map_changed = False
            start_region_map_changed = False
            finish_region_map_changed = False

            # check if object is newly created
            if self.instance.pk is None:
                new = True
            else:
                # check did any of the maps change
                old_route = MarathonRoute.objects.get(pk=self.instance.pk)

                self.instance.map_changed = self.cleaned_data["map"] != str(old_route.map)
                start_region_map_changed = self.cleaned_data["start_region_map"] != str(old_route.start_region_map)
                finish_region_map_changed = self.cleaned_data["finish_region_map"] != str(old_route.finish_region_map)

            # parse geoJSON if new or map field was changed
            if self.instance.map_changed or new:
                with open(self.instance.map.path_full) as f:
                    parsed = parse_geojson(f)
                    self.instance.parsed_map = str(parsed)

            if start_region_map_changed or new:
                with open(self.instance.start_region_map.path_full) as f:
                    parsed = parse_geojson(f)
                    self.instance.parsed_start_region_map = str(parsed)

            if finish_region_map_changed or new:
                with open(self.instance.finish_region_map.path_full) as f:
                    parsed = parse_geojson(f)
                    self.instance.parsed_finish_region_map = str(parsed)

            return super().save(**kwargs)
