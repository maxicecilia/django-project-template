# -*- coding: utf-8 -*-
from ..base import LOGGING

DEBUG = True

LOGGING['handlers']['file'] = {
    'level': 'DEBUG',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': '/home/webapp/logs/app.log',
    'maxBytes': 1024 * 1024 * 5,  # 5 MB
    'backupCount': 2,
    'formatter': 'verbose',
}

LOGGING['loggers']['django.request']['handlers'] = ['file']
LOGGING['loggers']['']['handlers'] = ['file']
LOGGING['loggers']['']['level'] = 'DEBUG'
