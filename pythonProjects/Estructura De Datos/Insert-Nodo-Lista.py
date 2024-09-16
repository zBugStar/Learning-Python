class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None or self.cabeza.valor >= nuevo_nodo.valor:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.valor < nuevo_nodo.valor:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def to_list(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado


def ordenamiento_por_insercion(vector):
    lista = ListaEnlazada()
    for valor in vector:
        lista.insertar(valor)
    return lista.to_list()


# Ejemplo de uso
vector = [4, 2, 7, 1, 3]
ordenado = ordenamiento_por_insercion(vector)
print(ordenado)  # Salida: [1, 2, 3, 4, 7]
