from django.db import models

class Servico(models.Model):
    nome = models.CharField('Serviço', max_length=255)
    descricao = models.TextField('Descrição')
    preco  = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    tempo =  models.PositiveIntegerField('Tempo de atendimento (em minutos)')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def  __str__(self):
        return self.nome
