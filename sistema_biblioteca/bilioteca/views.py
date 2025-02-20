from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Alunos, Autor, Livros, Emprestimos

from .serializers import AlunosSerializer, AutorSerializer, LivrosSerializer, EmprestimosSerializer
# Create your views here.

class AlunosViewSet(ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class EmprestimosViewSet(ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer