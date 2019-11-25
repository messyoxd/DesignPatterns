
class ChainOfResponsability:

    def checa_enumeration(self, dado, enum):
        for item in enum:
            if item[1] == dado:
                return item[0]
        return None

    def handle(self):
        pass
