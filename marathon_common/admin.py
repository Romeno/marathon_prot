from django.contrib import admin
from . import models

admin.site.register(models.Marathon)
admin.site.register(models.MarathonRoute)