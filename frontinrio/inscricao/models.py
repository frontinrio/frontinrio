from django.db import models


class Inscricao(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        unique_together = ('nome', 'email')


