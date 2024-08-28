import numpy as np


def pedirTemperatura():
    while True:
        entrada = input("Ingrese una temperatura en grados Celsius o 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            return None
        try:
            temperatura = float(entrada)
            return temperatura
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número o 'fin'.")


def main():
    temperaturas = []
    limite = 10

    print(f"Ingrese hasta {limite} temperaturas. Ingrese 'fin' para terminar antes.")
    while len(temperaturas) < limite:
        temp = pedirTemperatura()
        if temp is None:
            break
        temperaturas.append(temp)

    if not temperaturas:
        print("No se ingresaron temperaturas.")
        return

    tempArray = np.array(temperaturas)

    tempMax = np.max(tempArray)
    tempMin = np.min(tempArray)
    tempProm = np.mean(tempArray)

    print(f"Temperatura máxima: {tempMax} °C")
    print(f"Temperatura mínima: {tempMin} °C")
    print(f"Temperatura promedio: {tempProm:.2f} °C")

    temperarurasSobrePromedio = tempArray[tempArray > tempProm]
    print("Temperaturas por encima del promedio:")
    for temp in temperarurasSobrePromedio:
        print(f"{temp} °C")


if __name__ == "__main__":
    main()
