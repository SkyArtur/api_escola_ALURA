from escola.views import *


class ListaDeAlunosMatriculadosNoCursoViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaDeAlunosMatriculadosNoCursoSerializer
