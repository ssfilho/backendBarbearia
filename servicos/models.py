from django.db import models

class Service(models.Model):
    nome = models.CharField(max_length=100,null=True)
    tempo = models.IntegerField(null=True)
    valor = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nome} - Tempo: {self.tempo} min - Valor: R$ {self.valor}"
    class Meta:
        app_label = "servicos"
