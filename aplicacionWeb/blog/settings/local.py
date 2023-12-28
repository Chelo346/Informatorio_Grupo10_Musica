from .base import *

# Database
# http://docs.djangoproyect.com/en/4.2/ref/settings/#database


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proyectoblog',
        'USER': 'root',
        'PASSWORD': '1877',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
