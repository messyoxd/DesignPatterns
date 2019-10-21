class Singleton(type):

    __instancia=None

    @staticmethod
    def getInstance():

        if Singleton.__instancia == None:

            Singleton.__instancia = Singleton()
            return Singleton.__instancia
            
        else:
            return Singleton.__instancia