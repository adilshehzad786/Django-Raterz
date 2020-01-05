"""
Django settings for review project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from machina import MACHINA_MAIN_TEMPLATE_DIR
from machina import MACHINA_MAIN_STATIC_DIR
from oscar.defaults import  *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Your Secret Key Here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'users.apps.UsersConfig',
    'blogger.apps.BloggerConfig',

'django.contrib.sites',
    'calculator.apps.CalculatorConfig',
    'freecourses.apps.FreecoursesConfig',
    'elearning.apps.ElearningConfig',
    'homepage.apps.HomepageConfig',
    'coder.apps.CoderConfig',
    'crispy_forms',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoproject.apps.DjangoprojectConfig',
    'axes',
    'widget_tweaks',
    'pinax.comments',
    'sslserver',
    'simple_history',
    'admin_honeypot',
    'captcha',
    'pinax.ratings',
    'django_comments',
    'django_comments_xtd',
    'djrichtextfield',
    'reviews',
    'djangoseo',
'django_social_share',
    'django_user_agents',

    'martor',
    'reversion_compare',





# Machina dependencies:
    'mptt',
    'haystack',
    'taggit',
    'storages',
    'froala_editor',



    # Machina apps:
    'machina',
    'machina.apps.forum',
    'machina.apps.forum_conversation',
    'machina.apps.forum_conversation.forum_attachments',
    'machina.apps.forum_conversation.forum_polls',
    'machina.apps.forum_feeds',
    'machina.apps.forum_moderation',
    'machina.apps.forum_search',
    'machina.apps.forum_tracking',
    'machina.apps.forum_member',
    'machina.apps.forum_permission',



]

SITE_ID = 1
DJRICHTEXTFIELD_CONFIG = {
    'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}
FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url')
USE_FROALA_EDITOR=True
PINAX_RATINGS_CATEGORY_CHOICES = {
        "app.Photo": {
            "exposure": "How good is the exposure?",
            "framing": "How well was the photo framed?",
            "saturation": "How would you rate the saturation?"
        },
        "app.Story": {
            "grammar": "Good grammar?",
            "complete": "Is the story complete?",
            "compelling": "Is the article compelling?"
        }
    }
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
'django_user_agents.middleware.UserAgentMiddleware',





]

SILENCED_SYSTEM_CHECKS = ['axes.W003']

ROOT_URLCONF = 'review.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'djangoproject/../templates'),MACHINA_MAIN_TEMPLATE_DIR,],


         'APP_DIRS': True,


        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'machina.core.context_processors.metadata',

            ],
        },
    },
]
CACHES = {
'default': {
'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
},
'machina_attachments': {
'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
'LOCATION': '/tmp',
}
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR,'whoosh_index'),
    },
}

WSGI_APPLICATION = 'review.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    MACHINA_MAIN_STATIC_DIR

]


MACHINA_DEFAULT_AUTHENTICATED_USER_FORUM_PERMISSIONS = [
    'can_see_forum',
    'can_read_forum',
    'can_start_new_topics',
    'can_reply_to_topics',
    'can_edit_own_posts',
    'can_post_without_approval',
    'can_create_polls',
    'can_vote_in_polls',
    'can_download_file',
    'can_post_announcements',
    'can_delete_own_posts',
    'can_attach_file',
    
    'can_attach_file - Can attach file',

    'can_read_forum',
    'can_post_stickies',
    'can_vote_in_polls',

]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_PATH = os.path.realpath(os.path.dirname(__file__))

TEMPLATE_DIRS = (


    os.path.join(SETTINGS_PATH, r'C:\Users\Windows 10\PycharmProjects\review\templates\djangoproject'),
)


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
AXES_ENABLED = False

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL='blog-home'
LOGIN_URL='login'


MAX_UPLOAD_SIZE = "5242880"
#azure

DEFAULT_FILE_STORAGE = 'djangoproject.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'djangoproject.custom_azure.AzureStaticStorage'

STATIC_LOCATION = "mypublic-container"
MEDIA_LOCATION = "media"

AZURE_ACCOUNT_NAME = "Your Secret Key Here"
AZURE_CUSTOM_DOMAIN = f'Your Secret Key Here'
STATIC_URL = f'Your Secret Key Here'
MEDIA_URL = f'Your Secret Key Here'

if DEBUG:
     
    EMAIL_BACKEND = "Your Secret Key Here"
    SENDGRID_API_KEY = "Your Secret Key Here"

    #EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    #EMAIL_HOST = 'smtp.gmail.com'
    #EMAIL_USE_TLS = True
    #EMAIL_PORT = 587
    #EMAIL_HOST_USER = 'ufoneu5a786@gmail.com'
    #EMAIL_HOST_PASSWORD = '@followme'


    




