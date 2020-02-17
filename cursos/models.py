from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=255)


class Leccion(models.Model):
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Preguntas(models.Model):
    leccion = models.ForeignKey(Leccion, null=True, blank=True, on_delete=models.CASCADE)
    Pregunta = models.CharField(max_length=255)





