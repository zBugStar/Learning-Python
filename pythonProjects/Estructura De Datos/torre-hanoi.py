def numeroDeMovimeintos(n):
    return 2 ** n - 1


def inicializarTorre(n):
    origen = []
    destino = []
    auxiliar = []

    for i in range(n, 0, -1):
        origen.append(i)

    return origen, destino, auxiliar


def moverDisco(origen, destino, auxiliar):
    destino.apped(origen.pop())
    print(f"Movimiento {i}")
    print(f"Origen: {origen}")
    print(f"Auxiliar: {auxiliar}")
    print(f"Destino: {destino}")



numeroDeDiscos = 3
for i in range(1, numeroDeMovimeintos(numeroDeDiscos)):

    if i % 3 == 1:
        moverDisco(origen, destino)
    elif i % 3 == 2:
        moverDisco(origen, auxiliar)
    else:
        moverDisco(auxiliar, destino)
    print()
