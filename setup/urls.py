from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import (
    AlunoViewSet, CursoViewSet, MatriculaviewSet,
    ListaDeMatriculasDoAlunoViewSet, ListaDeAlunosMatriculadosNoCursoViewSet
)

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, 'Alunos')
router.register('cursos', CursoViewSet, 'Cursos')
router.register('matriculas', MatriculaviewSet, 'Matrículas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaDeMatriculasDoAlunoViewSet.as_view()),
    path('curso/<int:pk>/matriculas/', ListaDeAlunosMatriculadosNoCursoViewSet.as_view())
]
