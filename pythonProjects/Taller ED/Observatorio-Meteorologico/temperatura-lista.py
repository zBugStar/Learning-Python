# Función para pedir una temperatura al usuario
def pedir_temperatura():
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
    limite = 10  # Puedes ajustar el límite según lo que necesites

    print(f"Ingrese hasta {limite} temperaturas. Ingrese 'fin' para terminar antes.")
    while len(temperaturas) < limite:
        temp = pedir_temperatura()
        if temp is None:
            break
        temperaturas.append(temp)

    if not temperaturas:
        print("No se ingresaron temperaturas.")
        return

    tempMax = max(temperaturas)
    tempMin = min(temperaturas)
    tempProm = sum(temperaturas) / len(temperaturas)

    print(f"Temperatura máxima: {tempMax} °C")
    print(f"Temperatura mínima: {tempMin} °C")
    print(f"Temperatura promedio: {tempProm:.2f} °C")

    temperaturasSobreProm = [temp for temp in temperaturas if temp > tempProm]
    print("Temperaturas por encima del promedio:")
    for temp in temperaturasSobreProm:
        print(f"{temp} °C")


if __name__ == "__main__":
    main()
