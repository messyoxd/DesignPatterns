from ChainOfResponsability import ChainOfResponsability
class DataNascimentoHandler(ChainOfResponsability):

    def __init__(self, next=None):
        self._next = next

    def handle(self, dados, campo):
        if campo == "Data de nascimento":
            aux = dados
            data = ""
            for item in aux.split("/"):
                data += item+"-"
            data = data[:-1]
            return data
        else:
            if self._next != None:
                return self._next.handle(dados,campo)
            else:
                return None
