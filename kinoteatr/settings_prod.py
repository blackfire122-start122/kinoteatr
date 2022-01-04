import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'wqjranewq-insecuwq-d!%m8qw8r20iwzqwqsaw2(s05(^1&k6*re0$49z3(-jzo+u5$_&@#3)s)q'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = 'gsambir519@gmail.com'
EMAIL_HOST_PASSWORD = 'tytpassword123!i'
DEFAULT_FROM_EMAIL = 'gsambir519@gmail.com'
EMAIL_USE_TLS = True

# tytpass321!i