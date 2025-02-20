from rest_framework.serializers import ModelSerializer
from .models import Alunos, Autor, Livros, Emprestimos

class AlunosSerializer(ModelSerializer):
    class Meta: 
        model = Alunos
        fields = '__all__'

class AutorSerializer(ModelSerializer):
    class Meta: 
        model = Autor
        fields = '__all__'

class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'

class EmprestimosSerializer(ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = '__all__'