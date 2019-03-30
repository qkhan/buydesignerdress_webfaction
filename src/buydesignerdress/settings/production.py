"""
Django settings for buydesignerdress project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=0cc0gy2(j!i3e3vvd)w@_n)0$9d4d2)_s9@n1j=m0#1s%)gsv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'phonenumber_field',
    'multiselectfield',
    'floppyforms',
    'crispy_forms',
    'django_archive',
    'ckeditor',
    'ckeditor_uploader',
    'cloudinary',
    'accounts',
    'products',
    'items',
    'carts',
    'orders',
    'search',
    'tags',
    'billing',
    'addresses',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'accounts.MyUser'

ROOT_URLCONF = 'buydesignerdress.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'buydesignerdress.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#STATIC_URL = '/static/'

#STATICFILES_DIRS = [
	#os.path.join(BASE_DIR, "static_my_proj"),
	##'/var/www/static/',
#]
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")
#
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

STATIC_URL = '/static/'
#STATICFILES_DIRS = (
        #os.path.join(BASE_DIR, "static"),
#)
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static_my_proj"),
	#'/var/www/static/',
]

STATIC_ROOT = "/home/qaisar/webapps/buydesignerdress_static_root/"

MEDIA_URL = '/media/'
MEDIA_ROOT = "/home/qaisar/webapps/buydesignerdress_media_root/"

LOGOUT_REDIRECT_URL = '/register/'

CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_CONFIGS = {
#     'awesome_ckeditor': {
#         'toolbar': 'Basic',
#     },
# }

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#     },
# }

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'width': 380,
        'height': 196,
    }
}


import logging.config
LOGGING_CONFIG = None
import os
LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()
#print("DEBUG: LOG LEVEL", LOGLEVEL)
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        # 'logfile': {
        #     'level':LOGLEVEL,
        #     'class':'logging.handlers.RotatingFileHandler',
        #     'filename': '/vagrant/src/apps.log',
        #     'maxBytes': 50000,
        #     'backupCount': 2,
        #     'formatter': 'standard',
        # },
        # 'database_logfile': {
        #     'level':'DEBUG',
        #     'class':'logging.handlers.RotatingFileHandler',
        #     'filename': 'database.log',
        #     'maxBytes': 50000,
        #     'backupCount': 2,
        #     'formatter': 'standard',
        # },

    },
    'loggers': {
    # root logger
        '': {
            'level': LOGLEVEL,
            #'handlers': ['console', 'logfile'],
            'handlers': ['console'],
        },
        'myproject': {
            'level': LOGLEVEL,
            #'handlers': ['console', 'logfile'],
            'handlers': ['console'],
            # required to avoid double logging with root logger
            'propagate': False,
        },
        # 'django.db.backends': {
        #     'handlers': ['database_logfile'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
})
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
        cloud_name = "dmvnudxsw", 
        api_key = "113854372633178", 
        api_secret = "gA96t9MeAQQS1KKad7Q7RppZjAQ" 
)
#Environment variable: CLOUDINARY_URL=cloudinary://113854372633178:gA96t9MeAQQS1KKad7Q7RppZjAQ@dmvnudxsw

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': '/vagrant/src/debug.log',
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'myproject.custom': {
#             'handlers': ['console', 'mail_admins', 'file'],
#             'level': 'DEBUG',
#         }
#     }
# }


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#         },
#     },
# }
# LOG_LEVEL = 'DEBUG'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#     },
#     'handlers': {
#         # 'null': {
#         #     'level':'DEBUG',
#         #     'class':'logging.NullHandler',
#         # },
#         'logfile': {
#             'level':'WARNING',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': 'apps.log',
#             'maxBytes': 50000,
#             'backupCount': 2,
#             'formatter': 'standard',
#         },
#         'database_logfile': {
#             'level':LOG_LEVEL,
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': 'database.log',
#             'maxBytes': 50000,
#             'backupCount': 2,
#             'formatter': 'standard',
#         },
#         'console':{
#             'level':LOG_LEVEL,
#             'class':'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler'
#             # Only send emails when DEBUG = False
#             #'filters': ['require_debug_false'],
#         },
#     },
#     'loggers': {
#         'root': {
#             'level': 'DEBUG',
#             'handlers': ['console']
#         },
#         'django': {
#             'handlers':['console'],
#             'propagate': True,
#             'level':'WARN',
#         },
#         'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': False,
#         },
#         'django.db.backends': {
#             'handlers': ['database_logfile'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         'apps': {
#             'handlers': ['console', 'logfile', 'mail_admins'],
#             'level': 'DEBUG',
#         },
#         'classes.photo': {
#             'handlers': ['console', 'logfile', 'mail_admins'],
#             'level': 'DEBUG',
#         },
#         '': {
#           'handlers': ['console'],
#            'level': 'DEBUG',
#         },
#     }
# }
