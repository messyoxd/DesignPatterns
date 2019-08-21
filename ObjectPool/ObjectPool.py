'''
Object pool é um padrão que pode ser apreveitado em situações
em que se instanciar uma classe pode ser muito custoso e então
cria-se uma classe que acumula objetos custosos de se instanciar 
para que tenha um ganho de performance
'''

class Recurso:
    #variavel estática
    __valor = 0

    def setValor(self, valor):
        self.__valor = 0

    def getValor(self):
        return self.__valor

class ObjectPool:

    #variaveis estáticas
    __instance = None
    __recursos = []

    def __init__(self):
        if ObjectPool.__instance != None:
            print("Object Pool é um singleton!")

    @staticmethod
    def getInstancia():
        if ObjectPool.__instance == None:
            ObjectPool.__instance = ObjectPool()
            return ObjectPool.__instance
        else:
            return ObjectPool.__instance

    def insertRecurso(self, recurso):
        recurso.setValor(0)
        self.__recursos.append(recurso)

    def getRecurso(self):
        if len(self.__recursos)>0:
            return self.__recursos.pop(0)
        else:
            print("Não há recursos disponiveis")

def main():
    #instanciar ObjectPool
    pool = ObjectPool.getInstancia()
    #instanciar recurso
    recurso = Recurso()
    recurso.setValor(10)
    #printar o endereço de memoria
    print(str(recurso) + " valor: "+str(recurso.getValor()))
    #guardar recurso na object pool
    pool.insertRecurso(recurso)
    #mudar o valor da referencia da variavel do recurso
    recurso = None
    print(recurso)
    #pegar o mesmo recurso da object pool
    recurso = pool.getRecurso()
    #printar para mostrar que está no mesmo lugar de memoria que antes
    print(str(recurso)+" valor: "+str(recurso.getValor()))

if __name__ == "__main__":
    main()