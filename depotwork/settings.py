# coding:utf-8
from unipath import Path

PROJECT_DIR = Path(__file__).parent

from decouple import config

import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# DATABASES = {
# 'default': dj_database_url.config(
#       default = config('DATABASE_URL'))
# }

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = '01asb8%!ma51=-%u4=q^or%!n^ol^1vpp+zy*@_uve2x*ayi@^'

ALLOWED_HOSTS = ['127.0.0.1']
# 自定义的变量
REDIRECT_FIELD_NAME = 'next'

PAGINATOR_NUM = 5

AVATAR_IMAGE_WIDTH = 600

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'south',
    'depotwork.activities',
    'depotwork.articles',
    'depotwork.auth',
    'depotwork.core',
    'depotwork.feeds',
    'depotwork.messages',
    'depotwork.questions',
    'depotwork.search',

    #feture
    'depotwork.apps.asset',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'depotwork.urls'

WSGI_APPLICATION = 'depotwork.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# USE_TZ = False

# LANGUAGES = (
#     ('en', 'English'),
#     ('pt-br', 'Portuguese'),
#     ('es', 'Spanish'),
#     ('zh-cn','Chinese')
# )

LOCALE_PATHS = (PROJECT_DIR.child('locale'), )

DATE_FORMAT = 'Y/m/d'
DATETIME_FORMAT = u'Y年m月d日  H:m:s'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = PROJECT_DIR.parent.child('staticfile')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/feeds/'

ALLOWED_SIGNUP_DOMAINS = ['*']

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0644