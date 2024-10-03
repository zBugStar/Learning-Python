class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def agregar(self, nuevo_nodo):
        actual = self
        while actual.next is not None:
            actual = actual.next
        actual.next = nuevo_nodo

# Ejemplo de uso
n = Node(2)       # Nodo inicial con valor 2
n2 = Node(3)      # Nodo nuevo con valor 3
n3 = Node(5)
n.agregar(n2)
n.agregar(n3)# Agregamos el nodo n2 al final de la lista

# Mostrar el valor del siguiente nodo después de n
print(n.next.data)  # Salida: 3
