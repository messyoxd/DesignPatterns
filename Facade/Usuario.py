class Usuario:

    def __init__(self, nome, senha, email):
        self.__nome=nome
        self.__senha=senha
        self.__email=email

    def __repr__(self):
        return "\nnome: "+self.__nome+"\n"+"senha: "+self.__senha+"\n"+"email: "+self.__email+"\n"