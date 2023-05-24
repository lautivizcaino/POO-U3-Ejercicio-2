from manejaSabores import ManejadorSabores
from sabor import Sabor
class Helado:
    __gramos=float
    __precio=float
    __sabores=list
    def __init__(self,gramos,precio):
        self.__gramos=gramos
        self.__precio=precio
        self.__sabores=[]
    def agregarSabor(self,sabor):
        self.__sabores.append(sabor)

    def getGramos(self):
        return self.__gramos
    def getPrecio(self):
        return self.__precio
    def getSabores(self):
        return self.__sabores
    def getSabor(self,NumSabor):
        for sabor in self.__sabores:
            if sabor.getID()==NumSabor:
                return sabor
    
            
    def __str__(self) -> str:
        sabores=''
        i=0
        for sabor in self.__sabores:
            if i<len(self.__sabores)-1:
                sabores+=str(sabor.getNomSabor()) + ','
            else:
                sabores+=str(sabor.getNomSabor())
            i+=1
        return '%s %s %s'%(self.__gramos,self.__precio,sabores)
