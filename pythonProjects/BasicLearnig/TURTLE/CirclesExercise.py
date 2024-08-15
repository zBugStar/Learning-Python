import turtle

screen = turtle.getscreen()
turtle = turtle.Turtle()

turtle.circle(40)
turtle.up()
turtle.goto(80, 0)
turtle.down()
turtle.circle(40)
turtle.up()
turtle.goto(160, 0)
turtle.down()
turtle.circle(40)
turtle.up()
turtle.goto(240, 0)
turtle.down()
turtle.circle(40)

cordenadaX = 0
turtle.begin_fill()
for i in range(0, 4):
    # Aqui dibujamos nuestro circulo
    turtle.up()
    turtle.goto(cordenadaX, 100)
    turtle.down()
    turtle.circle(40)

    # Movemos las coordenadas para dibujar el nuevo circulo
    cordenadaX += 80

turtle.end_fill()
screen.mainloop()
