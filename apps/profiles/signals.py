from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import InstructorProfile

# Señal para crear automáticamente un perfil de instructor cuando se crea un nuevo usuario que es instructor.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_instructor_profile(sender, instance, created, **kwargs):
    # Crear un perfil de instructor cuando se crea un nuevo usuario que es instructor.
    if created and instance.is_instructor:
        InstructorProfile.objects.create(user=instance)
