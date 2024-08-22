# Codigo hecho por Juan Diego Orozco Meza

class Coche:
    def __init__(self, marca, modelo, year, color, nivelCombustible, encendido):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
        self.nivelCombustible = nivelCombustible
        self.encendido = False

    def encender(self):
        if self.encendido:
            print("El coche ya está encendido")
        else:
            self.encendido = True
            print("El coche se ha encendido")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El coche se ha apagado")

    def acelerar(self, nivelCombustible):
        if self.encendido:
            print("El coche está acelerando")
            self.nivelCombustible -= 1
            print("El nivel de combustible es:", self.nivelCombustible)

        if nivelCombustible < 2:
            print("El coche está apagado, no hay conbustible")
            self.apagar()

    def repostar(self):
        if self.nivelCombustible < 1:
            print("El coche está repostando")
            self.nivelCombustible = 10

        if self.nivelCombustible == 12:
            print("El coche ya está lleno de combustible")
            print("El nivel de combustible es:", self.nivelCombustible)
