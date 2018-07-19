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
from django.urls import path, include

from marathon_signal import views

urlpatterns = [
    # path('new/incident', views.signal_medical_incident),
    # path('new/danger', views.signal_danger),
    #
    # path('list', views.get_signals),
    # path('list/incident', views.get_signals),
    # path('list/danger', views.get_signals),
    #
    # path('list/danger/types', views.get_danger_types),
    #
    # path('list/incident/severities', views.get_incident_severities),
    # path('list/danger/severities', views.get_danger_severities),
]
