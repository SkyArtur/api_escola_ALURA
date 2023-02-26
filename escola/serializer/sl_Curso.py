from escola.serializer import *


class CursoSerializer(serializers.ModelSerializer):
    nivel = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'descricao', 'nivel', 'ativo']

    @staticmethod
    def get_nivel(obj):
        return obj.get_nivel_display()
