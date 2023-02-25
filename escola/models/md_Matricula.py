from escola.models import *


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.CharField(max_length=1, choices=TURNO, default='M')
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id:0>9} - {self.turno} - {self.aluno.nome} - {self.curso.descricao}'
