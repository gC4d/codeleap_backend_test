from __future__ import annotations

import logging
from os import getenv

logger = logging.getLogger(__name__)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv("DB_NAME", default="postgres"),
        'USER': getenv("DB_USER", default="postgres"),
        'PASSWORD': getenv("DB_PASSWORD", default="postgres"),
        'HOST': getenv("DB_HOST", default="localhost"),
        'PORT': getenv("DB_PORT", default="5432"),
    }
}