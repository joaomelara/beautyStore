from django.db import models

class Produto(models.Model):
    id_produtobeleza = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=255)
    marca = models.TextField(max_length=255)
    valor = models.FloatField()
    estoque = models.IntegerField()


# Create your models here.
