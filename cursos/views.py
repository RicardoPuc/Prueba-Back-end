from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import CursoSerializer, LeccionSerializer, PreguntasSerializer
from .models import Curso, Leccion, Preguntas


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('name')
    serializer_class =  CursoSerializer

class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all().order_by('name')
    serializer_class = LeccionSerializer

class PreguntasViewSet(viewsets.ModelViewSet):
    queryset = Preguntas.objects.all().order_by('Pregunta')
    serializer_class = PreguntasSerializer