from .module import Module
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from ..fields import OrderField

# Modelo base para los elementos que tienen un propietario.


class ItemBase(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_owned')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    # Representación en cadena del objeto, mostrando su título.

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    image = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()

# Modelo de contenido genérico que puede asociarse a cualquier tipo de objeto dentro de un módulo.


class Content(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='contents')
    # Tipo de contenido genérico asociado al objeto.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
                                     'model__in': ['text', 'file', 'image', 'video']})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    # Campo que determina el orden de los contenidos dentro de un módulo.
    order = OrderField(blank=True, for_fields=['module'])
