from ChainOfResponsability import ChainOfResponsability

class TimeFavoritoHandler(ChainOfResponsability):

    def __init__(self, next=None):
        self._next = next
        self._times = (
                ("CE", "Ceará"),
                ("FOR", "Fortaleza"),
                ("FER", "Ferroviário"),)

    def handle(self, dados, campo):
        if campo == "Time favorito":
            time = super().checa_enumeration(dados, self._times)
            if time == None:
                time = "-"
            return time
        else:
            if self._next != None:
                return self._next.handle(dados,campo)
            else:
                return None
