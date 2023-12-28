from .base import *

<<<<<<< HEAD
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
=======
#para usar bd mysql (pip install mysqlclient)
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DATABASES = {
    "default":{
        "ENGINE": "django.db.backends.mysql",
        "NAME": "proyecto_musica",
        "USER": "root",
        "PASSWORD": "1877",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
>>>>>>> 22b0fbae35aae288d2314b611f3efb30586647c5
