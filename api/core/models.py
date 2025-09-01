from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return self.nome


