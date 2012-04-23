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

    def __unicode__(self):
        return self.nome


class Checkout(models.Model):
    codigo = models.CharField(max_length=100)
    inscricao = models.ForeignKey(Inscricao)

    def __unicode__(self):
        return "%s (%s - %s)" % (self.codigo, self.inscricao.nome, self.inscricao.email)


