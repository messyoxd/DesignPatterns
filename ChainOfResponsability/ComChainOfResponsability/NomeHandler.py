from ChainOfResponsability import ChainOfResponsability
class NomeHandler(ChainOfResponsability):

    def __init__(self, next=None):
        self._next = next

    def handle(self, dados, campo):
        if campo == "Nome":
            aux = dados
            nome = ""
            for parte in aux.split(" "):
                nome += parte[0].upper() + parte[1:].lower()+" "
            nome = nome[:-1]
            return nome
        else:
            if self._next != None:
                return self._next.handle(dados,campo)
            else:
                return None
