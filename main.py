from manejaSabores import ManejadorSabores
from manejaHelados import ManejadorHelados
from menu import Menu
def test():
    listaSabores=ManejadorSabores()
    listaSabores.leerArchivo()
    print(listaSabores)
    listaHelados=ManejadorHelados()
    menu=Menu()
    menu.opciones(listaSabores,listaHelados)
if __name__=='__main__':
    test()