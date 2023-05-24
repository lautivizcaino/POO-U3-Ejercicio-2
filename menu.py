from manejaHelados import ManejadorHelados
from manejaSabores import ManejadorSabores
class Menu:
    __opcion:int
    def __init__(self):
        self.__opcion=6
    def opciones(self,listaSabores,listaHelados):
        while self.__opcion!=0:
            print('\n1 - Registar helado\n2 - Nombre de 5 sabores\n3 - Total de gramos vendidos\n4 - Mostrar sabores vendidos\n5 - Determinar importe total recaudado\n0 - Salir\n')
            self.__opcion=int(input('Ingrese la opcion a ejecutar: '))
            if self.__opcion==1:
                print('\nINCISO 1')
                listaHelados.registrarHelado(listaSabores)
                print(listaHelados)
            elif self.__opcion==2:
                print('\nINCISO 2')
                listaHelados.mostrar5Sabores(listaSabores)

            elif self.__opcion==3:
                print('\nINCISO 3')
                listaHelados.estimarGramosVendidos()

            elif self.__opcion==4:
                print('\nINCISO 4')
                listaSabores.mostrarSaboresVendidos(listaHelados)

            elif self.__opcion==5:
                print('\nINCISO 5')
                listaHelados.mostrarImporteTotal()
        else:
            print('\nHa salido del sistema')