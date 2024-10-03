def hanoi(n, origen, destino, auxiliar):
    """
    Función recursiva para resolver la Torre de Hanoi.

    Parámetros:
    - n: número de discos.
    - origen: la torre de la cual se moverán los discos.
    - destino: la torre a la cual se moverán los discos.
    - auxiliar: la torre auxiliar para ayudar en el proceso.
    """
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    # Mover n-1 discos de la torre origen a la torre auxiliar.
    hanoi(n - 1, origen, auxiliar, destino)

    # Mover el disco restante (el más grande) de la torre origen a la torre destino.
    print(f"Mover disco {n} de {origen} a {destino}")

    # Mover los n-1 discos de la torre auxiliar a la torre destino.
    hanoi(n - 1, auxiliar, destino, origen)

# Ejemplo de uso:
n = 5  # Número de discos
hanoi(n, 'A', 'C', 'B')  # A: origen, C: destino, B: auxiliar