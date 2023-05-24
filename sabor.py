class Sabor:
    __idSabor=int
    __ingredientes=str
    __nombreSabor=str
    def __init__(self,idSabor,ingredientes,nombreSabor):
        self.__idSabor=idSabor
        self.__ingredientes=ingredientes
        self.__nombreSabor=nombreSabor
    
    def getID(self):
        return self.__idSabor
    def getIngr(self):
        return self.__ingredientes
    def getNomSabor(self):
        return self.__nombreSabor

    def __str__(self) -> str:
        return '%s %s %s'%(self.__idSabor,self.__ingredientes,self.__nombreSabor)