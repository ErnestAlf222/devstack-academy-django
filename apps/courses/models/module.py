from django.db import models
from .course import Course

# Modelo que representa un módulo dentro de un curso


class Module(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.course} - {self.title}"
