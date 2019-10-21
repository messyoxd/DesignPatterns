
class Carteira:

    def __init__(self, id, valor):
        self.id = id
        self.__valor = valor

    def getValor(self):
        return self.__valor

    def addFundos(self,valor_adicionado):
        self.__valor+=valor_adicionado

if __name__ == "__main__":

    minha_carteira = Carteira("123",100)

    print(minha_carteira.getValor())
    print(minha_carteira.id)

    try:
        print(minha_carteira.__valor)
    except Exception as ex:
        print(ex)
    minha_carteira.addFundos(50)
    print(minha_carteira.__dict__)
