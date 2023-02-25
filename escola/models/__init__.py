from django.db import models

NIVEL = (
    ('B', 'Básico'),
    ('I', 'Intermediário'),
    ('A', 'Avançado')
)

TURNO = (
    ('M', 'Matutino'),
    ('V', 'Vespertino'),
    ('N', 'Noturno')
)

from .md_Aluno import Aluno
from .md_Curso import Curso
from .md_Matricula import Matricula

