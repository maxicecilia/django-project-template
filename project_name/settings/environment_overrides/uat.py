# -*- coding: utf-8 -*-
import os

RABBITMQ_USER = 'profiles_uat'
RABBITMQ_PASSWORD = 'Chutrux5=73spUdU'
RABBITMQ_VHOST = "/profiles_uat"
RABBITMQ_HOST = "mq-dev01.int.ngeo.com"
BROKER_URL = 'amqp://{0}:{1}@{2}{3}'.format(RABBITMQ_USER, RABBITMQ_PASSWORD,
                                            RABBITMQ_HOST, RABBITMQ_VHOST)

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DATABASE_ENGINE',
            'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_NAME', 'profiles'),
        'USER': os.environ.get('DATABASE_USER', 'profiles'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'profiles'),
        'HOST': os.environ.get('DATABASE_HOST', 'profiles-uat-db01.int.ngeo.com'),  # NOQA
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}

#  Tag for logcenter2
SYSLOG_IDENT = 'PROFILES_UAT_APP'
SYSLOG_IDENT_CELERY = 'PROFILES_UAT_CELERY'