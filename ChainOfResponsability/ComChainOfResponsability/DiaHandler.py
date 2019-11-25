from ChainOfResponsability import ChainOfResponsability

class DiaHandler(ChainOfResponsability):

    def __init__(self, next=None):
        self._next = next
        self._dias = (
            ("Segunda","1"),
            ("Terça","2"),
            ("Quarta","3"),
            ("Quinta","4"),
            ("Sexta","5"),
            ("Sábado","6"),
            ("Domingo","7"),)

    def handle(self, dados, campo):
        if campo == "Dia da entrevista":
            dia = super().checa_enumeration(dados, self._dias)
            if dia == None:
                dia = "-"
            return dia
        else:
            if self._next != None:
                return self._next.handle(dados,campo)
            else:
                return None
