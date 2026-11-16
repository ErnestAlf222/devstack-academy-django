from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    # Representación en cadena de la categoría
    def __str__(self):
        return self.name
