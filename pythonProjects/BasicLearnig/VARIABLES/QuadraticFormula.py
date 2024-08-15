print("Quadratic Formula")

sideA = float(input("Enter side A: "))
sideB = float(input("Enter side B: "))
sideC = float(input("Enter side C: "))

x1 = ((-sideB + (sideB**2 - 4*sideA*sideC)**0.5) / (2*sideA))
x2 = ((-sideB - (sideB**2 - 4*sideA*sideC)**0.5) / (2*sideA))

print("The roots are", x1, "and", x2)
