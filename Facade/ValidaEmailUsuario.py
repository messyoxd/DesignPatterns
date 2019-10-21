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
        
