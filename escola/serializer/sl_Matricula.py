from escola.serializer import *


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'turno', 'ativo']
