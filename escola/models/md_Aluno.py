from escola.models import *


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ('nome', '-data_nascimento')

    def __str__(self):
        return f'{self.nome}'


