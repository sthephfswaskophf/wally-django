from django.db import models

class Devedor (models.Model):

    id = models.AutoField(primarykey=True)
    name = models.CharField('Nome/Razão Social', max_length=80, blank=True, null=True)
    id_tax = models.BigIntegerField('CNPJ/CPF', max_length=20)
    id_espaider = models.IntegerField('ID Espaider', max_length=10)
    contabil = models.DecimalField('Contábil', max_digits=15, blank=False, decimal_places=2, default='0')
    risco = models.DecimalField('Risco', max_digits=15, blank=False, decimal_places=2, default='0')
    wallet_type = models.CharField(max_length=20, blank=False, default='MASSIFICADO PF',
                                   choices=(('MASSIFICADO PF', 'MASSIFICADO PF'),
                                    ('MASSIFICADO PJ', 'MASSIFICADO PJ'),
                                    ('AUTOS', 'AUTOS'),
                                    ('ALTO TICKET', 'ALTO TICKET'),
                                    ))
    phone_1 = models.CharField('Telefone', max_length=11)
    phone_2 = models.CharField('Telefone', max_length=11)
    phone_hot = models.CharField('Telefone Hot', max_length=11)
    phone_whatsapp = models.CharField('Whatsapp', max_length=11)
    status_negociacao = models.CharField(max_length=20, blank=False, default='NEGOCIAR',
                                         choices=(('NEGOCIAR', 'NEGOCIAR'),
                                             ('POTENCIAL', 'POTENCIAL'),
                                             ('PROPOSTA EM ANÁLISE', 'PROPOSTA EM ANÁLISE'),
                                             ('PROPOSTA APROVADA', 'PROPOSTA APROVADA'),
                                             ('PROPOSTA NEGADA', 'PROPOSTA NEGADA'),
                                             ('PROPOSTA EXPURGADA', 'PROPOSTA EXPURGADA'),
                                             ('PROPOSTA EXPURGA', 'PROPOSTA EXPURGADA'),
                                             ('ACORDO SEM ENTRADA', 'ACORDO SEM ENTRADA'),
                                             ('ACORDO PAGO', 'ACORDO PAGO'),
                                             ('FORMALIZADO', 'FORMALIZADO'),
                                             ('ACORDO EM DIA', 'ACORDO EM DIA'),
                                             ('ACORDO EXTERNO', 'ACORDO EXTERNO'),
                                             ('ACORDO QUITADO', 'ACORDO QUITADO'),
                                             ('DESINDICADO', 'DESINDICADO'),
                                             ('ACORDO ATIVO', 'ACORDO ATIVO'),
                                             ('NÃO ATUAR', 'NÃO ATUAR'),
                                             ))
    user_agent = models.CharField('NEGOCIADOR', max_length=50, blank=False)

    cpc_status = models.CharField(max_length=20, blank=False, default='SIM',
                                   choices=(('SIM', 'SIM'),
                                    ('NÃO', 'NÃO')
                                    ))
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    observacoes_status = models.TextField('Observações', max_length=500, blank=True)






