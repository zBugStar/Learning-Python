import turtle
import random

screen = turtle.getscreen()
screen.setup(1400,700)
screen.title("Carrera de tortugas")

#Configuracion de playerOne 
playerOne = turtle.Turtle()
playerOne.shape("turtle")
playerOne.color("Blue")
playerOne.shapesize(2,2,2)
playerOne.up()
playerOne.goto(-600, 100)

playerOne.goto(600,100)
playerOne.down()
playerOne.circle(40)
playerOne.up()
playerOne.goto(-600,140)

#Configuramos el playerTwo
playerTwo = turtle.Turtle()
playerTwo.shape("turtle")
playerTwo.color("Green")
playerTwo.shapesize(2,2,2)
playerTwo.up()
playerTwo.goto(-600, -100)

playerTwo.goto(600,-100)
playerTwo.down()
playerTwo.circle(40)
playerTwo.up()
playerTwo.goto(-600,-60)

dado = [1,2,3,4,5,6]

for i in range(30):
    if playerOne.pos() >= (600,140):
        print("Player One won")
        break
    elif playerOne.pos() >= (600,-60):
        print("Player Tow won")
        break
    else:
        playerOne_Turn = input("Presiona enter para tirar el dado")
        dadoResultado = random.choice(dado)
        print("El resultado del lazamiento es:  " + str(dadoResultado))
        print("El numero de pasos sera: "+ str(20*int(dadoResultado)))
        playerOne.fd(20*int(dadoResultado))
        
        playerTwo_Turn = input("Presiona enter para tirar el dado")
        dadoResultado = random.choice(dado)
        print("El resultado del lazamiento es:  " + str(dadoResultado))
        print("El numero de pasos sera: "+str(20*int(dadoResultado)))
        playerTwo.fd(20*int(dadoResultado))
        
    
    



