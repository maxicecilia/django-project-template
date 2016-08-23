# -*- coding: utf-8 -*-
from ..base import INSTALLED_APPS, LOGGING

# Django Nose
INSTALLED_APPS += (
    'django_nose',
)

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging
LOGGING['handlers']['file'] = {
    'level': 'DEBUG',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': 'app.log',
    'maxBytes': 1024 * 1024 * 3,  # 5 MB
    'backupCount': 1,
    'formatter': 'verbose',
}

LOGGING['loggers']['django.request']['handlers'] = ['file']
LOGGING['loggers']['']['handlers'] = ['file']
LOGGING['loggers']['']['level'] = 'DEBUG'
LOGGING['loggers']['django.db.backends'] = {
    'handlers': ['null'],  # Quiet by default!
    'propagate': False,
    'level': 'DEBUG',
}
