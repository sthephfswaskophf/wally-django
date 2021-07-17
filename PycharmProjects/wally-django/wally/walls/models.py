from django.db import models

class Devedor (models.Model):

    id = models.AutoField(primarykey=True)
    name = models.CharField('Nome/Razão Social' max_length=50, blank=True, null=True)
    id_tax = models.BigIntegerField('CNPJ/CPF')
    id_espaider = models.IntegerField('ID Espaider')
    phone_1 = models.IntegerField('Telefone')
    phone_2 = models.IntegerField('Telefone')
    phone_hot = models.IntegerField('Telefone Hot')
    phone_whatsapp = models.IntegerField('Whatsapp')






