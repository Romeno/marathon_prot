"""
Django settings for marathon project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .local_settings import *

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'rest_framework',
    'tinymce',

    'marathon_chronotrack.apps.MarathonChronotrackConfig',
    'marathon_marathons.apps.MarathonMarathonsConfig',
    'marathon_common.apps.FlatblocksAppConfig',
    'marathon_common.apps.MarathonCommonConfig',

    'marathon_medic.apps.MarathonMedicConfig',
    'marathon_signal.apps.MarathonSignalConfig',
    'marathon_task.apps.MarathonTaskConfig',
    'marathon_messaging.apps.MarathonMessagingConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marathon_utils.middleware.MarathonExceptionsMiddleware',
]

ROOT_URLCONF = 'marathon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'marathon.wsgi.application'


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

##########################################
# Internationalization
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
]

########################################
# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

MEDIA_URL = '/media/'

########################################
# Rest framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

########################################
# Grappelli
GRAPPELLI_ADMIN_TITLE = _("Marathon control system")


########################################
# File browser
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_MAX_UPLOAD_SIZE = 50*1024*1024
FILEBROWSER_NORMALIZE_FILENAME = False
FILEBROWSER_OVERWRITE_EXISTING = False
FILEBROWSER_DEFAULT_PERMISSIONS = 0o766
FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', ''],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.xlsx', '.docx', '.djvu', ''],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.ogv'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p', '.ogg'],
    'GeoJSON': ['.json', '.geojson'],
}
FILEBROWSER_SELECT_FORMATS = {
    'file': ['Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
    'geojson': ['GeoJSON'],
}

########################################
# Tinymce
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 50,
    'relative_urls': False,
    'remove_script_host': False,
    'convert_urls': True,

    'plugins': "autolink,lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,inlinepopups,autosave",

    # no styleselect
    'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline,strikethrough,|,forecolor,backcolor,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "undo,redo,|,cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,link,unlink,anchor,charmap,image,media,|,cleanup,code,preview,help,",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|print,|,fullscreen",
    'theme_advanced_buttons4': "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak,restoredraft",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,

    'theme_advanced_font_sizes': "9px,10px,11px,12px,13px,14px,15px,16px,17px,18px,20px,22px,24px,26px,28px,30px,36px,54px,72px",
    'theme_advanced_fonts': "Andale Mono=andale mono,times;Arial=arial,helvetica,sans-serif;Arial Black=arial black,avant garde;Book Antiqua=book antiqua,palatino;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Georgia=georgia,palatino;Helvetica=helvetica;Impact=impact,chicago;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco;Times New Roman=times new roman,times;Trebuchet MS=trebuchet ms,geneva;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats",

    'width': '90%',
    'height': 700,

    # for styleselect
    # 'theme_advanced_styles': "Header 1=header1;Header 2=header2;Header 3=header3;Table Row=tableRow1",
    'theme_advanced_blockformats': "p,div,h1,h2,h3,h4,h5,h6,blockquote",

    # 'content_css': "/static/css/content-" + CC_STATIC_VERSION + ".css",

    # Drop lists for link/image/media/template dialogs
    'external_link_list_url': "lists/link_list.js",
    'external_image_list_url': "lists/image_list.js",
    'media_external_list_url': "lists/media_list.js",

    # 'template_templates': [
    #     {
    #         'title': '2 Columns',
    #         'src': '/static/templates/2columns.html',
    #         'description': '2 Columns.'
    #     },
    # ],
}