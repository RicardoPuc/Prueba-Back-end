from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Leccion(models.Model):
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Preguntas(models.Model):
    leccion = models.ForeignKey(Leccion, null=True, blank=True, on_delete=models.CASCADE)
    Pregunta = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Pregunta

class Respuestas(models.Model):
    preguntas=models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    respuesta=models.CharField(max_length=200)
    votos=models.IntegerField(default=0)
    
    def __str__(self):
        return self.respuesta





