temperatura = []

programaOn = True

print("Bienvenido al Observatorio Meteorológico")
print("Vamos a ingresar unas temperaturas para analizarlas")
print("El maximo de temperaturas a ingresar es de 24")

while programaOn:
    temp = input("Ingrese la temperatura, si desea no ingresar mas temperaturas escriba fin: ")

    if temp == "fin":
        programaOn = False

    elif len(temperatura) == 24:
        programaOn = False

    else:
        temperatura.append(temp)

temperaturaConv = [int(i) for i in temperatura]

print("Las temperaturas ingresadas son: ", temperatura)
print("La temperatura mas baja es: ", min(temperatura))
print("La temperatura mas alta es: ", max(temperatura))
print("La temperatura promedio es: ", sum(temperaturaConv) / len(temperaturaConv))

for i in range(len(temperatura)):
    if temperaturaConv[i] > sum(temperaturaConv) / len(temperaturaConv):
        print("La temperatura ", temperatura[i], " es mayor a la temperatura promedio")
