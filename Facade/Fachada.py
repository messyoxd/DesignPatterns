from Usuario import *
from ValidaSenhaUsuario import *
from ValidaEmailUsuario import *

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