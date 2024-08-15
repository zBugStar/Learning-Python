import turtle
import time

screen = turtle.getscreen()
screen.bgcolor("LightBlue")
screen.title("Pintando con turtle")

turtle = turtle.Turtle()
# Vamos a cambiar la forma de Turtle

turtle.shape("turtle")
# Definimos el estilo de nuestra tortuga
turtle.pen(pencolor = "white", fillcolor = "orange", speed = 10, pensize = 10)

# Shapesize sirve para cambiar el tamaño del puntero
turtle.shapesize(1,1,1)

# Aqui definimos la velocidad a la que queremos que vaya turtle
#turtle.speed(10)

# turtle.fillcolor("red") cambia el color del relleno
# turtle.pencolor("White") cambia el color de la tinta y el borde
# el .color hace los dos anteriores a la vez

#turtle.color("white","green")
time.sleep(0.5)
# Para hacer todos estos cambios en una sola linea de codigo potemos turtle.pen(Aqui van los parametros)
turtle.dot(50)
time.sleep(1)
turtle.undo()
# Aqui cambia,os el tamaño de la linea 
#turtle.pensize(5)


# Con el begin y end podemos pintar las figuras que hicimos
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

