# -*- coding: utf-8 -*-
import os
import raven
from ..base import BASE_DIR, INSTALLED_APPS

DEBUG = False
ALLOWED_HOSTS = []

# Raven
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': u'TBD',  # NOQA
    'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
}
