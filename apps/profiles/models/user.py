# Se extrae AbstractUser para personalizar el modelo de usuario
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        # Se intenta obtener el nombre completo del usuario, si no existe se usa el nombre de usuario
        return self.get_full_name() or self.username
