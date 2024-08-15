import turtle

screen = turtle.getscreen()
screen.setup(500, 500)
screen.bgcolor("lightblue")

turtle = turtle.Turtle()

turtle.shape("turtle")
turtle.pen(pencolor = "black", fillcolor = "yellow", speed = 10, pensize = 2)
turtle.shapesize(0.5,0.5,0.5)

# Creamos sus pies

turtle.up()
turtle.goto(-80,-120)
turtle.down()

turtle.begin_fill()
turtle.fd(50)
turtle.rt(90)
turtle.fd(20)
turtle.rt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(20)
turtle.rt(90)
turtle.end_fill()

turtle.up()
turtle.goto(20,-120)
turtle.down()

turtle.begin_fill()
turtle.fd(50)
turtle.rt(90)
turtle.fd(20)
turtle.rt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(20)
turtle.rt(90)
turtle.end_fill()


