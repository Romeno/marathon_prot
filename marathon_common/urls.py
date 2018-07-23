"""marathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path

from marathon_common import views

urlpatterns = [
    re_path('settings', views.get_settings),
    re_path('routes/(?P<id>\d+)/map', views.get_route_map),
    re_path('routes/(?P<id>\d+)/heights', views.get_route_heights),
    re_path('routes/(?P<id>\d+)/info', views.get_route_info),
    re_path('routes/(?P<id>\d+)/start_region_map', views.get_start_region_map),
    re_path('routes/(?P<id>\d+)/finish_region_map', views.get_finish_region_map),
    re_path('expo', views.get_expo_info),
    re_path('photo_frames', views.get_photo_frames),
]