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
        
