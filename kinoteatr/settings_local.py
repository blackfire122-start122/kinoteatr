import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-d!%m8%8r20iwzqmwo2(s05(^1&k68*0$49z3(-jyzo+u5$_&@#'

DEBUG = True

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'