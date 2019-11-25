class ValidaSenhaUsuario():

    @staticmethod
    def validar(senha):

        if(len(senha) > 6):

            return True

        else:

            False


class ValidaEmailUsuario():

    @staticmethod
    def validar(email):

        # ex: email@gmail.com -> tem '@' e '.com' então é válido
        if(len(email.split("@")) == 2 and len(email.split("@")[1].split(".com")) == 2):

            return True

        else:

            False


class Usuario:

    def __init__(self, nome, senha, email):

        if ValidaSenhaUsuario.validar(senha) and ValidaEmailUsuario.validar(email):
            self.__nome = nome
            self.__senha = senha
            self.__email = email

    def __repr__(self):
        try:
            return "\nnome: "+self.__nome+"\n"+"senha: "+self.__senha+"\n"+"email: "+self.__email+"\n"
        except:
            return "\nErro! Senha inválida ou Email inválido!\n"


class Fachada:

    def criaUsuario(self, nome, senha, email):
        '''
            Retorna instancia de Usuario com o nome,senha e 
            email da entrada ou erro
        '''
        return Usuario(nome, senha, email)


if __name__ == "__main__":

    fachada = Fachada()

    nome = input()
    senha = input()
    email = input()

    usuario = fachada.criaUsuario(nome, senha, email)

    print(usuario)
