from django.db import models


class Inscricao(models.Model):
    STATUS = (
        ('p', 'Pendente'),
        ('a', 'Aprovada'),
        ('r', 'Rejeitada'),
    )

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS)
    data_inscricao = models.DateField(auto_now_add=True)


