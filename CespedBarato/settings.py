# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qyqltmp1w0(u39)d(pyx(a(e%42l)ysk!j%c$+&unyl82g7c!p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['cespedbarato.ec', 'cespedbarato.com.ec']


# Application definition
TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',

        ],
    },
},]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CespedBarato.urls'

WSGI_APPLICATION = 'CespedBarato.wsgi.application'

#DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'rawrkyco_cespedbarato',
#         'USER': 'rawrkyco_makubex',
#        'PASSWORD': 'monica22',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#    }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_USE_SSL = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'info@cespedbarato.ec'
EMAIL_HOST_PASSWORD = 'Info321!'
EMAIL_PORT = 465

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/home1/rawrkyco/public_html/cespedbarato/static'
STATIC_URL = '/static/'