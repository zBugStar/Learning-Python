class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class listaEnlazada:

    def __init__(self):
        self.cabeza = None

    def ordenamiento(self, lista):

        while lista:
            if self.cabeza is None or self.cabeza.dato >= lista.dato:
                lista.siguiente = self.cabeza
                self.cabeza = lista
            else:
                actual = self.cabeza
                while actual.siguiente is not None and actual.siguiente.dato < lista.dato:
                    actual = actual.siguiente
                lista.siguiente = actual.siguiente
                actual.siguiente = lista
            lista = lista.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
lista.insertar(10)
lista.insertar(6)