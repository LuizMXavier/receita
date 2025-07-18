from django.db import models

# Create your models here.
class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.T