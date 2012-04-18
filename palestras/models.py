from django.db import models


class Palestra(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    autor = models.CharField(max_length=100)
    minicv = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True, null=True)
