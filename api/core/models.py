from django.db import models


class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    local = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome


class Lote(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='lotes')
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.evento.nome}"


class Ingresso(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='ingressos')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.lote.nome} - {self.quantidade} ingressos"
