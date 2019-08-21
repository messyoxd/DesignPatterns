'''
O padrão builder se refere à uma classe que instancia outras classes através de uma
'montagem' de objetos menos complexos que se unem no objeto final
'''

class Aluno:
    def __init__(self):
        self.__cadastro = None
        self.__pontoFocal = None

    def alunoInformacoes(self):
        print("Matricula  : "+self.__cadastro.matricula)
        print("Ponto Focal: "+self.__pontoFocal.pf)

    def setCadastro(self, Cadastro):
        self.__cadastro = Cadastro

    def setPontoFocal(self, Registro):
        self.__pontoFocal = Registro

class Cadastro:
    matricula = None

class PontoFocal:
    pf = None

class Builder:
    def getCadastro(self):
        pass
    def getPontoFocal(self):
        pass

class AlunoIFCEBuilder(Builder):

    def getCadastro(self):
        cadastro = Cadastro()
        cadastro.matricula = "123456789"
        return cadastro

    def getPontoFocal(self):
        pontoFocal = PontoFocal()
        pontoFocal.pf = "IFCE"
        return pontoFocal

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def construct(self):
        aluno = Aluno()

        aluno.setCadastro(self.__builder.getCadastro())
        aluno.setPontoFocal(self.__builder.getPontoFocal())

        return aluno

if __name__ == "__main__":
    alunoIFCEBuilder = AlunoIFCEBuilder()
    montador = Director()
    montador.setBuilder(alunoIFCEBuilder)
    aluno = montador.construct()
    aluno.alunoInformacoes()
