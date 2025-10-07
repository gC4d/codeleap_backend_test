from __future__ import annotations

import logging
import os
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Use DATABASE_URL if provided (Heroku), otherwise use individual environment variables
if 'DATABASE_URL' in os.environ:
    url = urlparse(os.environ.get('DATABASE_URL'))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME", default="postgres"),
            'USER': os.getenv("DB_USER", default="postgres"),
            'PASSWORD': os.getenv("DB_PASSWORD", default="postgres"),
            'HOST': os.getenv("DB_HOST", default="localhost"),
            'PORT': os.getenv("DB_PORT", default="5432"),
        }
    }