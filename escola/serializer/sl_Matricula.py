from escola.serializer import *


class MatriculaSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    curso = serializers.ReadOnlyField(source='curso.codigo')
    turno = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'turno', 'ativo']

    @staticmethod
    def get_turno(obj):
        return obj.get_turno_display()
