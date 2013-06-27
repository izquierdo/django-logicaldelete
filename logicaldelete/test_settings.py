import os
import django

if django.VERSION[:2] >= (1, 3):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASE_ENGINE = 'sqlite3'

INSTALLED_APPS = [
    'logicaldelete',
    'logicaldelete.tests',
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SECRET_KEY = "ht0255o6f11ym5s%ln*&amp;b*#jw3rwh(6g+)$ls9(0=ywoteus$v"
