from ChainOfResponsability import ChainOfResponsability

class ComidaHandler(ChainOfResponsability):

    def __init__(self, next=None):
        self._next = next

    def handle(self, dados, campo):
        if campo == "Comida favorita":
            return dados
        else:
            if self._next != None:
                return self._next.handle(dados,campo)
            else:
                return None
