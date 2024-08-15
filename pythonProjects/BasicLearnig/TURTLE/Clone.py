import turtle

screen = turtle.getscreen()
screen.setup(1200,700)
screen.bgcolor("White")

turtle = turtle.Turtle()
cloneTurtle = turtle.clone()

turtle.shape("turtle")
turtle.pen(pencolor = "brown", fillcolor = "lightblue", speed = 10, pensize = 10)
turtle.shapesize(2,2,2)

cloneTurtle.shape("turtle")
cloneTurtle.pen(pencolor = "purple", fillcolor = "pink", speed = 10, pensize = 10)
cloneTurtle.shapesize(2,2,2)

turtle.circle(60)
cloneTurtle.circle(80)

