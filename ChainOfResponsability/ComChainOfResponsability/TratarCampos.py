from ChainOfResponsability import ChainOfResponsability
class TratarCampos(ChainOfResponsability):

    def __init__(self, next):
        self._next = next

    def handle(self, dados, campo):
        return self._next.handle(dados, campo)
