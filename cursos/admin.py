from django.contrib import admin
from cursos.models import Curso, Leccion, Preguntas
# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    list_display=("name",)

class LeccionAdmin(admin.ModelAdmin):
    list_display=("name",)


class PreguntasAdmin(admin.ModelAdmin):
    list_display=("Pregunta",)


admin.site.register(Curso, CursosAdmin)
admin.site.register(Leccion, LeccionAdmin)
admin.site.register(Preguntas, PreguntasAdmin)