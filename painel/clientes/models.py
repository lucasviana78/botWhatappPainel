from django.db import models
from django.utils import timezone

# Create your models here.

class clientes (models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=80)
    email_painel = models.CharField(max_length=100)
    situacao = [
        (0, "Ativo"),
        (1, "Inativo")
    ]
    situacao = models.CharField(max_length=1, choices=situacao)



