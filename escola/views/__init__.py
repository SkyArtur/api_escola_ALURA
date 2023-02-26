from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.serializer import (
    Curso, CursoSerializer, Aluno, AlunoSerializer, Matricula,
    MatriculaSerializer, ListaDeMatriculasDoAlunoSerializer,
    ListaDeAlunosMatriculadosNoCursoSerializer
)

from .vws_Aluno import AlunoViewSet
from .vws_Curso import CursoViewSet
from .vws_Matricula import MatriculaviewSet
from .vws_ListaDeMatriculasDoAluno import ListaDeMatriculasDoAlunoViewSet
from .vws_ListaDeAlunosMatriculadosNoCurso import ListaDeAlunosMatriculadosNoCursoViewSet

