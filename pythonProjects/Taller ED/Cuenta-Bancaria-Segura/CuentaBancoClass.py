# Codigo hecho por Juan Diego Orozco Meza

class CuentaBancaria:
    def __init__(self, numeroCuenta, saldo, nombrePropietario):
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        self.nombrePropietario = nombrePropietario

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Se ha depositado:", cantidad)
        print("El saldo actual es:", self.saldo)

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
            print("El saldo actual es:", self.saldo)
        else:
            self.saldo -= cantidad
            print("Se ha retirado:", cantidad)
            print("El saldo actual es:", self.saldo)

    def consultarSaldo(self):
        print("El saldo actual es:", self.saldo)