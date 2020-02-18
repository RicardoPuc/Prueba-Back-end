from django.contrib import admin
from cursos.models import Curso, Leccion, Preguntas, Respuestas
# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    list_display=("name",)

class LeccionAdmin(admin.ModelAdmin):
    list_display=("name",)
    list_filter=("curso",)


class PreguntasAdmin(admin.ModelAdmin):
    list_display=("Pregunta",)


class RespuestasAdmin(admin.ModelAdmin):
    list_display=("respuesta", 'votos',)


admin.site.register(Curso, CursosAdmin)
admin.site.register(Leccion, LeccionAdmin)
admin.site.register(Preguntas, PreguntasAdmin)
admin.site.register(Respuestas, RespuestasAdmin)