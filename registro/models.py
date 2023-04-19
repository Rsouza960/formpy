from django.db import models

class Solicitacao(models.Model):
    nome_empresa = models.CharField(max_length=155)
    cnpj_cpf = models.CharField(max_length=14, verbose_name='CNPJ/CPF')
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numerocasa = models.CharField(max_length=5)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=20)
    uf = models.CharField(max_length=15)

