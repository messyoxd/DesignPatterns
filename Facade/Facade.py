class ValidaSenhaUsuario():

    __instancia=None

    @staticmethod
    def getInstance():

        if ValidaSenhaUsuario.__instancia == None:

            ValidaSenhaUsuario.__instancia = ValidaSenhaUsuario()
            return ValidaSenhaUsuario.__instancia
            
        else:
            return ValidaSenhaUsuario.__instancia
    
    def validar(self, senha):

        if(len(senha)>6):

            return True

        else:

            False
        
class ValidaEmailUsuario():

    __instancia=None

    @staticmethod
    def getInstance():

        if ValidaEmailUsuario.__instancia == None:

            ValidaEmailUsuario.__instancia = ValidaEmailUsuario()
            return ValidaEmailUsuario.__instancia
            
        else:
            return ValidaEmailUsuario.__instancia

    def validar(self, email):

        # ex: email@gmail.com -> tem '@' e '.com' então é válido
        if(len(email.split("@"))==2 and len(email.split("@")[1].split(".com"))==2):

            return True

        else:

            False
        


class Usuario:

    def __init__(self, nome, senha, email):
        self.__nome=nome
        self.__senha=senha
        self.__email=email

    def __repr__(self):
        return "\nnome: "+self.__nome+"\n"+"senha: "+self.__senha+"\n"+"email: "+self.__email+"\n"

class Fachada:

    def __init__(self):
        self.validaSenhaUsuario = ValidaSenhaUsuario.getInstance()
        self.validaEmailUsuario = ValidaEmailUsuario.getInstance()

    def criaUsuario(self,nome,senha,email):
        '''
            Retorna instancia de Usuario com o nome,senha e 
            email da entrada ou erro
        '''
        if not self.validaSenhaUsuario.validar(senha):
            return "Erro! Senha inválida!"
        
        if not self.validaEmailUsuario.validar(email):
            return "Erro! Email inválido!"

        return Usuario(nome, senha, email)

if __name__ == "__main__":

    fachada = Fachada()

    nome=input()
    senha=input()
    email=input()


    usuario = fachada.criaUsuario(nome, senha, email)

    print(usuario)