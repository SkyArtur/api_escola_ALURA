from escola.views import *


class MatriculaDoAlunoViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = MatriculaDoAlunoSerializer

