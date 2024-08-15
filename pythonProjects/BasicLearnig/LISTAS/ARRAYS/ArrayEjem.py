nombres = ["Juan", "Pedro", "Juan", "Maria"]
edades = [10, 11, 12]

nombres.append("Luis")
edades.insert(1, 14)

print(nombres.count("Juan"))
size = len(nombres)

print(nombres)

while "Juan" in nombres:
    replace = nombres.index("Juan")
    nombres[replace] = "Jhon"


print(nombres)
print(edades)
print(size)
