class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        
        nuevoNodo = Nodo(valor)
        if self.cabeza is None or self.cabeza.valor >= nuevoNodo.valor:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.valor < nuevoNodo.valor:
                actual = actual.siguiente
            nuevoNodo.siguiente = actual.siguiente
            actual.siguiente = nuevoNodo

    def resultadoLista(self):

        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado


def ordenamientoPorInsercion(vector):
    lista = ListaEnlazada()
    for valor in vector:
        lista.insertar(valor)
    return lista.resultadoLista()


vector = [4, 2, 7, 1, 3]
ordenado = ordenamientoPorInsercion(vector)
print("La lista ordenada de menor a mayor es: ")
print(ordenado)
