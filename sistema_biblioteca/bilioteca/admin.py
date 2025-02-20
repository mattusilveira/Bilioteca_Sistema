from django.contrib import admin

from .models import Alunos, Autor, Livros, Emprestimos
# Register your models here.

admin.site.register(Alunos)
admin.site.register(Autor)
admin.site.register(Livros)
admin.site.register(Emprestimos)