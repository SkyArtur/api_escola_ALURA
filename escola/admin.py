from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

# Register your models here.
admin.site.register(Matricula)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento', 'ativo')
    list_display_links = ('id', 'nome')
    list_editable = ('ativo',)
    list_per_page = 6
    list_filter = ('nome', 'cpf', 'rg', 'ativo')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel', 'ativo')
    list_display_links = ('id', 'codigo')
    list_editable = ('ativo',)
    list_filter = ('codigo', 'nivel', 'ativo')
