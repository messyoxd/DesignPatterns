'''
    Façade

    sistema de cadastro de usuarios

    O Façade irá servir de fachada para interfaciar um sistema
    mais complexo de forma mais simples

'''
from Fachada import *
if __name__ == "__main__":

    fachada = Fachada()

    nome=input()
    senha=input()
    email=input()


    usuario = fachada.criaUsuario(nome, senha, email)

    print(usuario)

