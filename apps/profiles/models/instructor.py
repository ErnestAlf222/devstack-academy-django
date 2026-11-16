from django.db import models
from django.conf import settings


class InstructorProfile(models.Model):
    user = models.OneToOneField(
        # Se usa el modelo de usuario personalizado definido en settings.AUTH_USER_MODEL
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # Campos del perfil del instructor
    bio = models.TextField(blank=True)
    photo = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    social_network = models.URLField(blank=True, null=True)

    # Representación en cadena del perfil del instructor
    def __str__(self):
        return f"Instructor: {self.user.get_full_name() or self.user.username}"
