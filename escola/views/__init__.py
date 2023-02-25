from rest_framework import viewsets
from escola.serializer import Curso, CursoSerializer, Aluno, AlunoSerializer, Matricula, MatriculaSerializer

from .vws_Aluno import AlunoViewSet
from .vws_Curso import CursoViewSet
from .vws_Matricula import MatriculaviewSet

