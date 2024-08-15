import turtle

screen = turtle.getscreen()
turtle = turtle.Turtle()

turtle.dot(60)
turtle.up()
turtle.goto(60,0)
turtle.down()
turtle.dot(60)
turtle.up()
turtle.goto(120,0)
turtle.down()
turtle.dot(60)
turtle.up()
turtle.goto(180,0)
turtle.down()
turtle.dot(60)

coordenadaX = 0 
for i in range (0,4):

    turtle.up()
    turtle.goto(coordenadaX,100)
    turtle.down()
    turtle.dot(60)
    coordenadaX += 60