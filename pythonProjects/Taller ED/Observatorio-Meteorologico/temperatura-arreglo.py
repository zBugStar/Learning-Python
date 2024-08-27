import numpy as np


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

    temp_array = np.array(temperaturas)

    temp_max = np.max(temp_array)
    temp_min = np.min(temp_array)
    temp_prom = np.mean(temp_array)

    print(f"Temperatura máxima: {temp_max} °C")
    print(f"Temperatura mínima: {temp_min} °C")
    print(f"Temperatura promedio: {temp_prom:.2f} °C")

    temperaturas_sobre_prom = temp_array[temp_array > temp_prom]
    print("Temperaturas por encima del promedio:")
    for temp in temperaturas_sobre_prom:
        print(f"{temp} °C")


if __name__ == "__main__":
    main()