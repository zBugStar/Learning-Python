import CocheClass

micoche = CocheClass.Coche("Ford", "Focus", 1998, "Azul", 13, False)
micoche.encender()
print(micoche.nivelCombustible)

while micoche.nivelCombustible > 0.1:
    micoche.acelerar(micoche.nivelCombustible)

