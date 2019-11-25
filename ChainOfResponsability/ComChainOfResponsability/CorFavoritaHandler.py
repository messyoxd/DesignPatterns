from ChainOfResponsability import ChainOfResponsability
class CorFavoritaHandler(ChainOfResponsability):

    def __init__(self, next=None):
        self._next = next
        self._cores = (
                ("Vermelho","VER"),
                ("Azul","AZ"),
                ("Verde","VERD"))

    def handle(self, dados, campo):
        if campo == "Cor favorita":
            cor = super().checa_enumeration(dados, self._cores)
            if cor == None:
                cor = "-"
            return cor
        else:
            if self._next != None:
                return self._next.handle(dados,campo)
            else:
                return None
