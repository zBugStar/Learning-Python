
pila = []
apertura = 0
cerradura = 0

ecuacion = input("Ingrese la ecuacion a realizar: ")
tamaño = len(ecuacion)

for i in range(tamaño):

    if ecuacion[i] == "(" or ecuacion[i] == "[" or ecuacion[i] == "{":
        pila.append(ecuacion[i])
        apertura += 1

    elif ecuacion[i] == ")" or ecuacion[i] == "]" or ecuacion[i] == "}":
        if len(pila) == 0:
            print("Error: hay un paréntesis de cierre sin su respectiva apertura.")
            break
        else:
            pila.pop()
        cerradura += 1

if apertura != cerradura:
    print("Error: hay un paréntesis de apertura sin su respectiva cierre.")
else:
    print("Los parentesis están balanceados.")

print(pila)
print(apertura)
print(cerradura)