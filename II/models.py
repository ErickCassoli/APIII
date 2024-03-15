from django.db import models


class Books(models.Model):
    sensor = models.BooleanField(default=False)
    botao = models.BooleanField(default=False)
    ligaRobo = models.BooleanField(default=False)
    resetContador = models.BooleanField(default=False)
    valorContagem = models.IntegerField(default=0)
