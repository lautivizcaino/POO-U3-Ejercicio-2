from sabor import Sabor
import csv
class ManejadorSabores:
    __listaSabores=list
    def __init__(self) -> None:
        self.__listaSabores=[]
    def agregarSabor(self,sabor):
        self.__listaSabores.append(sabor)
    def leerArchivo(self):
        file= open('sabores.csv',encoding="utf-8")
        reader= csv.reader(file,delimiter=';')
        for row in reader:
            unSabor=Sabor(int(row[0]),row[1],row[2])
            self.agregarSabor(unSabor)
        file.close()
    def buscaSabor(self,sabor):
        i=0
        while i<len(self.__listaSabores):
            if sabor==self.__listaSabores[i].getNomSabor():
                return self.__listaSabores[i]
                i=range(len(self.__listaSabores))
            i+=1
    
    def getLen(self):
        return len(self.__listaSabores)

    def mostrarMaximos(self,contador):
        indices=[]*5
        print('Helados más pedidos')
        for j in range(5):
            max=-1
            for i in range(len(contador)):
                if contador[i]>max:
                    max=contador[i]
                    indice=i
            contador[indice]=-1
            indices.append(indice)
            print('%s'%self.__listaSabores[indices[j]].getNomSabor())
            
    def mostrarSaboresVendidos(self,listaHelados):
        tipo=float(input('Ingrese tipo de helado: '))
        print('Sabores vendidos de %.2fg'%(tipo))
        for sabor in self.__listaSabores:
            if listaHelados.encontrarSaborVendido(tipo,sabor.getID())!=None:
                print(sabor.getNomSabor())

    def __str__(self):
        s=''
        for sabor in self.__listaSabores:
            s+=str(sabor) + '\n'
        return s