""" Implementação usando o padrão Builder """

import abc

class Festa:

    def __init__(self, nome, decoracao, fantasia, comidas):
        self.__decoracao = decoracao
        self.__fantasia = fantasia
        self.__comidas = comidas
        self.__nome = nome

    def __str__(self):
        return "nome: " + self.__nome + " | " + "decoração: " + self.__decoracao + " | " + " fantasia: " + self.__fantasia + " | " + " comidas: " + self.__comidas


class FestaBuilder(metaclass=abc.ABCMeta):

    def escolher(self):
        pass


class NatalBuilder(FestaBuilder):
    def set_decoracao(self, decoracao):
        self.__decoracao = decoracao

    def escolher(self):
        return Festa("Natal", self.__decoracao, "Papai noel", "Chester")


class NatalDirector:
    def __init__(self, builder):
        self.__builder = builder

    def decorar(self):
        self.__builder.set_decoracao("Arvore de natal")


class SaoJoaoBuilder(FestaBuilder):

    def set_fantasia(self, fantasia):
        self.__fantasia = fantasia

    def escolher(self):
        return Festa("São João", "Bandeirinhas", self.__fantasia, "Pamonha")


class SaoJoaoDirector:
    def __init__(self, builder):
        self.__builder = builder

    def decorar(self):
        self.__builder.set_fantasia("Camisa xadrez")


class HalloweenBuilder(FestaBuilder):

    def set_comidas(self, comidas):
        self.__comidas = comidas

    def escolher(self):
        return Festa("Halloween", "Jack-o'-lantern", "Fantasma", self.__comidas)


class HalloweenDirector:
    def __init__(self, builder):
        self.__builder = builder

    def decorar(self):
        self.__builder.set_comidas("Doces")


class OrganizadorDeFestas:

    def __init__(self):
        self.__festas = {}
        self.organizar()
        self.mostrar_festas()

    def organizar(self):
        natal_builder = NatalBuilder()
        natal_director = NatalDirector(natal_builder)
        natal_director.decorar()
        self.__festas['natal'] = natal_builder.escolher()

        sao_joao_builder = SaoJoaoBuilder()
        sao_joao_director = SaoJoaoDirector(sao_joao_builder)
        sao_joao_director.decorar()
        self.__festas['são joão'] = sao_joao_builder.escolher()

        halloween_builder = HalloweenBuilder()
        halloween_director = HalloweenDirector(halloween_builder)
        halloween_director.decorar()
        self.__festas['halloween'] = halloween_builder.escolher()

    def mostrar_festas(self):
        print("Festas à serem organizadas:")
        for key in self.__festas.keys():
            print(self.__festas[key])


if __name__ == "__main__":
    organizador = OrganizadorDeFestas()
