import turtle

screen = turtle.getscreen()
turtle = turtle.Turtle()

# Aqui creamos nuestro circulos 
turtle.circle(60)
turtle.circle(80)
turtle.circle(100)
turtle.circle(120)

# Con el Up y Down Subimos y bajamos nuestro lapiz
# Con el goto llevamos nuestro lapiz a unas coordenadas exactas
turtle.up()
turtle.goto(0,-100)
turtle.down()

# Con el dot dibujamos puntos
turtle.dot(60)

