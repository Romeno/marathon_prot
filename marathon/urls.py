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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLs should be before admin site URLs
    re_path(r'admin/', admin.site.urls),

    # re_path(r'', include('marathon_main.urls')),
    re_path(r'', include('marathon_common.urls')),

    re_path(r'^runners/', include('marathon_runner.urls')),

    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # re_path(r'^medics/', include('marathon_medic.urls')),
    # re_path(r'^judges/', include('marathon_judge.urls')),
    # re_path(r'^volunteers/', include('marathon_volunteer.urls')),
    # re_path(r'^transport/', include('marathon_transport.urls')),
    # re_path(r'^director/', include('marathon_director.urls')),



    # re_path(r'^messages/', include('marathon_message.urls')),
    # re_path(r'^tasks/', include('marathon_task.urls')),
    # re_path(r'^signals/', include('marathon_signal.urls')),
]

# if settings.DEBUG:
#     urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)