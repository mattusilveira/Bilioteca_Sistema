from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class Autor(models.Model):
    nome = models.CharField(max_length=155)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Alunos(models.Model):

    class Cursos(models.IntegerChoices):
        AGROPECUARIA = 1, "Agropecuária"
        INFORMATICA = 2, "Informática para Internet"
        QUIMICA = 3, "Química"

    nome = models.CharField(max_length=155)
    matricula = models.CharField(max_length=11)
    curso = models.IntegerField(choices=Cursos.choices, default=Cursos.INFORMATICA)

    class Meta:
        verbose_name = "aluno"
        verbose_name_plural = "alunos"

    def __str__(self):
        return self.nome


class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    ano_publicacao = models.DateField()

    class Meta:
        verbose_name = "livro"
        verbose_name_plural = "livros"

    def __str__(self):
        return self.titulo

class Emprestimos(models.Model):
    id_aluno = models.ForeignKey(Alunos, on_delete=models.PROTECT)
    id_livro = models.ForeignKey(Livros, on_delete=models.PROTECT)
    data_emprestimo = models.DateField(default=now)
    data_devolucao = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "emprestimo"
        verbose_name_plural = "emprestimos"

    def save(self, *args, **kwargs):
        if not self.data_devolucao:
            self.data_devolucao = self.data_emprestimo + timedelta(days=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"aluno_id: {self.id_aluno}"