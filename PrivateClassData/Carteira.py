
class Carteira:

    def __init__(self, id, valor):
        self.__id = id
        self.__valor = valor

    def getID(self):
        return self.__id

    def getValor(self):
        return self.__valor

if __name__ == "__main__":

    minha_carteira = Carteira("123",100)

    print(minha_carteira.getID())
    print(minha_carteira.getValor())
    try:
        print(minha_carteira.__id)
    except Exception as ex:
        print(ex)

    try:
        print(minha_carteira.__valor)
    except Exception as ex:
        print(ex)

    print(minha_carteira.__dict__)