from rest_framework import serializers
from .models import Curso, Leccion, Preguntas

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('name',)


class LeccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leccion
        fields = ('curso','name')


class PreguntasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Preguntas
        fields = ('leccion', 'Pregunta')