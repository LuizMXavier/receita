from django.db import models

# Create your models here.
class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=)