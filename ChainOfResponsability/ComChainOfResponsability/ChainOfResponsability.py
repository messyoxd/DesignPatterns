import abc
class ChainOfResponsability(metaclass=abc.ABCMeta):

    def checa_enumeration(self, dado, enum):
        for item in enum:
            if item[1] == dado:
                return item[0]
        return None

    @abc.abstractmethod
    def handle(self):
        pass
