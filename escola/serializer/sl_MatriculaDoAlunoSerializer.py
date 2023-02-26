from escola.serializer import *


class MatriculaDoAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    turno = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'turno']

    @staticmethod
    def get_turno(obj):
        return obj.get_turno_display()
