from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

from .sl_Aluno import AlunoSerializer
from .sl_Curso import CursoSerializer
from .sl_Matricula import MatriculaSerializer
from .sl_MatriculaDoAlunoSerializer import MatriculaDoAlunoSerializer
