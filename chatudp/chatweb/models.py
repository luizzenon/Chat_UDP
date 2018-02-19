from django.db import models

class SalaChat(models.Model):
    codigo_sala = models.IntegerField(blank=True)
    nome_sala = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return "{}: {}".format(self.codigo_sala, self.nome_sala)    


class Mensagem(models.Model):
    texto = models.CharField(max_length=50, blank=True)
    sala = models.ManyToManyField(SalaChat, blank=True)

    def __str__(self):
        return "{}: {}".format('texto', self.texto)

