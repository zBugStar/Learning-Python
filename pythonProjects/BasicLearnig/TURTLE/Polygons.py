import turtle

screen = turtle.getscreen()
turtle = turtle.Turtle()

numberSides = 5
sizeSides = 100

internalAngle = ((numberSides - 2)*180)/numberSides
externalAngle = 180 - internalAngle

for i in range(0, numberSides):
    
    turtle.fd(sizeSides)
    turtle.rt(externalAngle)
