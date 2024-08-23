import CocheClass

micoche = CocheClass.Coche("Ford", "Focus", 1998, "Azul", 13, False)
micoche.encender()
print(micoche.nivelCombustible)

simulaorOn = True

while simulaorOn:
    print("1. Encender")
    print("2. Apagar")
    print("3. Acelerar")
    print("4. Repostar")
    print("5. Salir")

    opcion = int(input("Introduce una opción: "))

    if opcion == 1:
        micoche.encender()
    elif opcion == 2:
        micoche.apagar()
    elif opcion == 3:
        micoche.acelerar(micoche.nivelCombustible)
    elif opcion == 4:
        micoche.repostar()
    elif opcion == 5:
        simulaorOn = False
    else:
        print("Introduce una opción válida")
