from django.db import models

# Create your models here.

class Suco(models.Model):
    nome = models.CharField(max_length=255)
    litros = models.FloatField()
    link = models.CharField(max_length=255, null=True)
    qtd_disp = models.IntegerField()

    class Meta:
        unique_together = ('nome', 'litros')
