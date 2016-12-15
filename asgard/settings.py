"""
Django settings for asgard project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lfe6(1teyq%ot=lt*mf=o9qsamx=&q++fnv&oe=qrd+ziyi68b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


AUTHENTICATION_BACKENDS = (
    'userprofile.auth.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend'
)

REGISTRATION_OPEN = False

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',

    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'django_extensions',

    # custom apps
    'userprofile',
    'access',
    'donations',

    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'asgard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

WSGI_APPLICATION = 'asgard.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CURRENCY_FORMAT = "EUR %.2f"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static-collected/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static-collected')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

ADMIN_TOOLS_MENU = 'asgard.menu.CustomMenu'

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
    'exclude_models': ('TimestampModel,Bookmark,DashboardPreferences,'
                       'Session,ContentType,LogEntry')
}

INTERNAL_IPS = ('172.16.42.1', '127.0.0.1')

CURRENCIES = ('EUR', )

from .rest_settings import *

from asgard.local_settings import *
