def verificarParentesis(cadena):
    simbolos = {')': '(', ']': '[', '}': '{'}

    pila = []

    for char in cadena:
        if char in simbolos.values():
            pila.append(char)
        elif char in simbolos.keys():
            if not pila or pila[-1] != simbolos[char]:
                return False
            pila.pop()

    return len(pila) == 0


# Ejemplos de uso
cadena1 = "Hola como estas))"
cadena2 = "{[(])}"
cadena3 = "{[()]}{[]}"

print(verificarParentesis(cadena1))  # Salida: True
print(verificarParentesis(cadena2))  # Salida: False
print(verificarParentesis(cadena3))  # Salida: True
