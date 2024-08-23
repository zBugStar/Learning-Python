import CuentaBancoClass

cuentas = [
    CuentaBancoClass.CuentaBancaria(116677, 1000, "Juan Diego"),
    CuentaBancoClass.CuentaBancaria(115577, 9000, "Jhon Doe")
]

confirmacion = True

while confirmacion:

    proceso = True
    cuentaActual = None
    cuenta = None

    print("Digite el numero de cuenta o 0 para salir: ")

    numeroCuenta = int(input())

    for cuenta in cuentas:
        if cuenta.numeroCuenta == numeroCuenta:
            cuentaActual = cuenta
            break

    if cuentaActual:
        while proceso:

            print("Bienvenido", cuentaActual.nombrePropietario)
            print("¿Que desea hacer?")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Consultar Saldo")
            print("4. Salir")

            opcion = int(input("Digite una opcion: "))

            if opcion == 1:
                cantidad = int(input("Digite la cantidad a depositar: "))
                cuentaActual.depositar(cantidad)
            elif opcion == 2:
                cantidad = int(input("Digite la cantidad a retirar: "))
                cuentaActual.retirar(cantidad)
            elif opcion == 3:
                cuentaActual.consultarSaldo()
            elif opcion == 4:
                proceso = False
            else:
                print("Opcion invalida")

            print("\n")

    elif numeroCuenta == 0:
        print("Gracias por usar nuestros servicios")
        confirmacion = False

    else:
        print("Numero de cuenta invalido")
        print("Intente de nuevo")
        print("\n")
