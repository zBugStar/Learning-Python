import CocheClass

miCoche = CocheClass.Coche("Ford", "Focus", 1998, "Azul", 1, False)
simuladorEncendido = True

while simuladorEncendido:
    print("1. Encender")
    print("2. Apagar")
    print("3. Acelerar")
    print("4. Repostar")
    print("5. Obtener nivel de combustible")
    print("6. Salir")

    opcion = int(input("Introduce una opción: "))

    if opcion == 1:
        miCoche.encender()
    elif opcion == 2:
        miCoche.apagar()
    elif opcion == 3:
        miCoche.acelerar(miCoche.nivelCombustible)
    elif opcion == 4:
        miCoche.repostar()
    elif opcion == 5:
        miCoche.obtenerNivelCombustible()
    elif opcion == 6:
        Encendido = False
    else:
        print("Introduce una opción válida")

    print("\n")
