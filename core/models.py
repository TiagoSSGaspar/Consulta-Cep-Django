from django.db import models


# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.endereco
