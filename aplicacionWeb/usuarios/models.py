from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefono = models.CharField(max_length = 255)
    domicilio = models.CharField(max_length = 255, blank = True, null = True)
    es_admin = models.BooleanField(default=False)

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     related_name="%(app_label)s_%(class)s_set",   # Cambia esto aquí
    #     related_query_name="%(app_label)s_%(class)ss", # Cambia esto aquí
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_name="%(app_label)s_%(class)s_set",   # Cambia esto aquí
    #     related_query_name="%(app_label)s_%(class)ss", # Cambia esto aquí
    # )