'''
O padrão builder se refere à uma classe que instancia outras classes através de uma
'montagem' de objetos menos complexos que se unem no objeto final
'''

class Aluno:
    def __init__(self):
        self.__cadastro = None
        self.__registro = None

    def alunoInformacoes(self):
        print("matricula: "+self.__cadastro.matricula)
        print("CPF      : "+self.__registro.CPF)

    def setCadastro(self, Cadastro):
        self.__cadastro = Cadastro

    def setRegistro(self, Registro):
        self.__registro = Registro

class Cadastro:
    matricula = None

class Registro:
    CPF = None

class Builder:
    def getCadastro(self):
        pass
    def getRegistro(self):
        pass

class AlunoBuilder(Builder):

    def getCadastro(self):
        cadastro = Cadastro()
        cadastro.matricula = "123456789"
        return cadastro

    def getRegistro(self):
        registro = Registro()
        registro.CPF = "123456789"
        return registro

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def construct(self):
        aluno = Aluno()

        aluno.setCadastro(self.__builder.getCadastro())
        aluno.setRegistro(self.__builder.getRegistro())

        return aluno

if __name__ == "__main__":
    alunoBuilder = AlunoBuilder()
    montador = Director()
    montador.setBuilder(alunoBuilder)
    aluno = montador.construct()
    aluno.alunoInformacoes()
