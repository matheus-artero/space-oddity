from django.db import models

# Create your models here.
class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=1)