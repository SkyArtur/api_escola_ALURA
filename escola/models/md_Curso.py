from escola.models import *


class Curso(models.Model):
    codigo = models.CharField(max_length=7, unique=True)
    descricao = models.CharField(max_length=150)
    nivel = models.CharField(max_length=1, choices=NIVEL, default='B')
    ativo = models.BooleanField(default=True)

    class Meta:
        oredering = ('codigo',)

    def __str__(self):
        return self.codigo
