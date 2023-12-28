from .base import *

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