""" Implementação com Fluent Interface """
import abc

class Festa:

    def __init__(self):
        self.__decoracao = "Nada"
        self.__fantasia = "Nada"
        self.__comidas = "Nada"
        self.__nome = "Nada"

    def nome(self, nome):
        self.__nome = nome
        return self

    def fantasia(self, fantasia):
        self.__fantasia = fantasia
        return self
    def comidas(self, comidas):
        self.__comidas = comidas
        return self
    def decoracao(self, decoracao):
        self.__decoracao = decoracao
        return self
    def __str__(self):
        return "nome: " + self.__nome + " | " + "decoração: " + self.__decoracao + " | " + " fantasia: " + self.__fantasia + " | " + " comidas: " + self.__comidas
        
class OrganizadorDeFestas:
    def __init__(self):
        self.__festas = {}
        self.organizar()
        self.mostrar_festas()
    def organizar(self):
        self.__festas['natal'] = Festa().nome('Natal').decoracao('Arvore de natal').fantasia('Papai noel').comidas('Chester')
        self.__festas['são joão'] = Festa().nome('São João').decoracao('Bandeirinhas').fantasia('Camisa xadrez').comidas('Pamonha')
        self.__festas['halloween'] = Festa().nome('Halloween').decoracao("Jack-o'-lantern").fantasia('Fantasma').comidas('Doces')
    def mostrar_festas(self):
        print("Festas à serem organizadas:")
        for key in self.__festas.keys():
            print(self.__festas[key])


if __name__ == "__main__":
    organizador = OrganizadorDeFestas()
