from django.db import models

class Devedor (models.Model):

    name = models.TextField()
    id_debtor = models.BigIntegerField()
    id_espaider = models.IntegerField()
    phone_1 = models.IntegerField()
    phone_2 = models.IntegerField()
    phone_hot = models.IntegerField()
    phone_whatsapp = models.IntegerField()


    id_debtor = models.ForeignKey("Devedor", on_delete=models.SET_NULL, null=True)



