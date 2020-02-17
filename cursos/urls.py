from django.urls import include, path
from rest_framework import routers
from . import views

router =  routers.DefaultRouter()
router.register(r'cursos',views.CursoViewSet)
router.register(r'lecciones',views.LeccionViewSet)
router.register(r'preguntas',views.PreguntasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]