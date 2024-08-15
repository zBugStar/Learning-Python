print("Converted moaned")

cop = float(input("¿What do you left in pesos? "))
sol = float(input("¿What do you left in soles? "))
reais = float(input("¿What do you left in reais? "))

convertedCop = cop*0.00026
convertedSol = sol*0.27
convertedReais = reais*0.20

print("The total COP's in dollar's is ", convertedCop)
print("The total soles in dollar's is ", convertedSol)
print("The total reais in dollar's is ", convertedReais)

totalDollars = convertedCop + convertedSol + convertedReais

print("The total in dollar's is ", totalDollars)