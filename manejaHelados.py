from helado import Helado
from manejaSabores import ManejadorSabores
from sabor import Sabor
class ManejadorHelados:
    __listaHelados=list
    def __init__(self):
        self.__listaHelados=[]
    def agregarHelado(self,helado):
        self.__listaHelados.append(helado)

    def registrarHelado(self,listaSabores):
        gramos=float(input('\nIngrese el tipo de helado: '))
        precio=float(input('Ingrese precio del helado: '))
        cant=int(input('Ingrese cantidad de sabores: '))
        unHelado=Helado(gramos,precio)
        for i in range(cant):
            unSabor=listaSabores.buscaSabor(input('Ingrese nombre del sabor: '))
            unHelado.agregarSabor(unSabor)
        self.agregarHelado(unHelado)

    def mostrar5Sabores(self,listaSabores):
        contador=[0]*listaSabores.getLen()
        for helado in self.__listaHelados:
            for sabor in helado.getSabores():
                contador[sabor.getID()-1]+=1
        listaSabores.mostrarMaximos(contador)

    def estimarGramosVendidos(self):
        numSabor=int(input('Ingrese numero de sabor: '))
        tot=0.0
        for helado in self.__listaHelados:
            sabor=helado.getSabor(numSabor)
            if sabor!=None:   
                tot+=helado.getGramos()/len(helado.getSabores())
        print('Cantidad de gramos vendidos:%.2f'%(tot))
    
    def encontrarSaborVendido(self,tipo,id):
        i=0
        while i<len(self.__listaHelados):
            if self.__listaHelados[i].getGramos()==tipo:
                unSabor=self.__listaHelados[i].getSabor(id)
                if unSabor!=None:
                    i=len(self.__listaHelados)
                else:
                    i+=1
            else:
                i+=1
        return unSabor
            
    def mostrarImporteTotal(self):
        tot=[0.0]*5
        for helado in self.__listaHelados:
            if helado.getGramos()==100:
                tot[0]+=helado.getPrecio()
            elif helado.getGramos()==150:
                tot[1]+=helado.getPrecio()
            elif helado.getGramos()==250:
                tot[2]+=helado.getPrecio()
            elif helado.getGramos()==500:
                tot[3]+=helado.getPrecio()
            elif helado.getGramos()==1000:
                tot[4]+=helado.getPrecio()
        TOTAL=0.0
        gramos=[100,150,200,500,1000]
        print('TIPO DE HELADO   IMPORTE RECAUDADO')
        for i in range(len(tot)):
            TOTAL+=tot[i]
            print('%sg                  %.2f'%(gramos[i],tot[i]))
        print('TOTAL RECAUDADO      %.2f'%TOTAL)
    def __str__(self) -> str:
        s=''
        for helado in self.__listaHelados:
            s+=str(helado) + '\n'
        return s