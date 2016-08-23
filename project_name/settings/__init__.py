# -*- coding: utf-8 -*-
"""
Overridable settings.
"""
import os


try:
    from .base import *  # NOQA
except ImportError:
    pass

try:
    from .environment_overrides.active import *  # NOQA
except:
    env = os.environ.get("{{project_name}}_ENV".upper(), 'development')

    try:
        m = __import__(
            '{{project_name}}.settings.environment_overrides.{}'.format(env),
            globals=globals(), locals=locals(), fromlist="*"
        )
        try:
            attrlist = m.__all__
        except AttributeError:
            attrlist = dir(m)
        for attr in [a for a in attrlist if '__' not in a]:
            globals()[attr] = getattr(m, attr)
    except ImportError:
        pass

try:
    from .local import *  # NOQA
except ImportError:
    pass
