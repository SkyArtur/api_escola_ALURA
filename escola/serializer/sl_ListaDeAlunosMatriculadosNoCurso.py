from escola.serializer import *


class ListaDeAlunosMatriculadosNoCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    turno = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['aluno', 'turno']

    @staticmethod
    def get_turno(obj):
        return obj.get_turno_display()
