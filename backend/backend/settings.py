"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%h+w*sf+6ozcj7&^_1m*p8626cq0q@b-kz+_4+t7n6@zg#%g9q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'channels_redis',
    'rest_framework',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'corsheaders',
    'huey.contrib.djhuey',
    'fuskar',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

ASGI_APPLICATION = 'backend.routing.application'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}

# allowed origins to make cross site requests
CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fuskardb',
        'USER': 'fuskar',
        'PASSWORD': 'fuskar',
        'HOST': 'localhost',
        'PORT': '5432',
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


# Celery config
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'


### Rest framework settings

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CACHE_URL = '/.fuskar-cache/'
CACHE_ROOT = os.path.join(BASE_DIR, '.fuskar-cache')


if DEBUG:
    MEDIA_PATH = MEDIA_ROOT
    CACHE_PATH = CACHE_ROOT
else:
    MEDIA_PATH = MEDIA_URL
    CACHE_PATH = CACHE_URL

## AI global variables

PREDICTION_MODES = [
    "knn",
    "svm",
    "direct-euclid"
]

PREDICTION_MODE = PREDICTION_MODES[0]

SVM_EMBEDDING_MAP = os.path.join(CACHE_PATH, 'cache', 'svm-embedding-map.pkl')
KNN_EMBEDDING_MAP = os.path.join(CACHE_PATH, 'cache', 'knn-embedding-map.pkl')
ENCODING_LIST = os.path.join(CACHE_PATH, 'cache', 'encoding-list.pkl')
PATH_TO_EMBEDDING_DICT = os.path.join(CACHE_PATH, 'cache', 'path-to-embedding-dict.pkl')
PCA_GRAPH = os.path.join(CACHE_PATH, 'images', 'pca-3d.png')

TRAIN_DIR = os.path.join(MEDIA_PATH, 'images')
# Confidence level. Higher is stricter. 
# Inverse of distance, where higher is looser
CONFIDENCE = 0.50
DISTANCE = 1 - CONFIDENCE
TARGET_EMOTIONS = ['surprise', 'calm', 'anger', 'fear']
ADJACENT_THRESHOLD = 20
