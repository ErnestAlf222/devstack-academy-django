from django.db import models
from .course import Course

# Modelo que representa un módulo dentro de un curso
from ..fields import OrderField


class Module(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Campo que determina el orden de los módulos dentro de un curso.
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return f"{self.course} - {self.title}"
