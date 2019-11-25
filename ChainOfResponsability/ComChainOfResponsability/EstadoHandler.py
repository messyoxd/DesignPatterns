from ChainOfResponsability import ChainOfResponsability
class EstadoHandler(ChainOfResponsability):

    def __init__(self, next=None):
        self._next = next
        self._estados = (
            ('Acre','AC'),
            ('Alagoas','AL'),
            ('Amapá','AP'),
            ('Amazonas','AM'),
            ('Bahia','BA'),
            ('Ceará','CE'),
            ('Distrito Federal','DF'),
            ('Espírito Santo','ES'),
            ('Goiás','GO'),
            ('Maranhão','MA'),
            ('Mato Grosso','MT'),
            ('Mato Grosso do Sul','MS'),
            ('Minas Gerais','MG'),
            ('Pará','PA'),
            ('Paraíba','PB'),
            ('Paraná','PR'),
            ('Pernambuco','PE'),
            ('Piauí','PI', ),
            ('Rio de Janeiro','RJ'),
            ('Rio Grande do Norte','RN'),
            ('Rio Grande do Sul','RS'),
            ('Rondônia','RO'),
            ('Roraima','RR'),
            ('Santa Catarina','SC'),
            ('São Paulo','SP'),
            ('Sergipe','SE'),
            ('Tocantins','TO'))

    def handle(self, dados, campo):
        if campo == "Estado":
            estado = super().checa_enumeration(dados, self._estados)
            if estado == None:
                estado = "-"
            return estado
        else:
            if self._next != None:
                return self._next.handle(dados,campo)
            else:
                return None
