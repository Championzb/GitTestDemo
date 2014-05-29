"""
Django settings for django_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.getcwd()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w7-@0_)!k_77+=(_#_t3j)uh9!k3ujxx*i&&fa9zumzqs&d5gw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
TEMPLATE_DIRS = (
    '/home/damon/Documents/Python/django-damon/django_test/templates',
    '/home/damon/Documents/Python/django-damon/django_test/article/templates',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'south',
    'whoosh',
    'haystack',
    'django.contrib.formtools',
    'userprofile',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_test.urls'

WSGI_APPLICATION = 'django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'test', 
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = PROJECT_DIR

STATIC_URL = '/static/'

STATICFILES_DIRS=(
    ('assets', os.path.join(os.getcwd(),'static/')),
)

MEDIA_ROOT = os.path.join(os.getcwd(),'static/')

LOGGING = {
    'version':1,
    'disable_existing_loggers': True,
    'formatters':{
        'standard':{
            'format':'%(asctime)s [%(levelname)s] %(name)s: %(message)s'  
        },    
    },
    'handlers':{
        'default':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/mylog.log',
            'maxBytes':1024*1024*5,
            'backupCount':5,
            'formatter':'standard',
        },
        'request_handler':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/django_request.log',
            'maxBytes':1024*1024*5,
            'backupCount':5,
            'formatter':'standard',
        },
    },
    'loggers':{
        '':{
            'handlers':['default'],
            'level':'DEBUG',
            'propagate':True
        },
        'django.request':{
            'handlers':['request_handler'],
            'level':'DEBUG',
            'propagate':False,
        }, 
    }
}

WHOOSH_INDEX = os.path.join(PROJECT_DIR,'whoosh/')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'
