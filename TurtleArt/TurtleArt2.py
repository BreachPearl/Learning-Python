from turtle import Turtle, Screen

sam=Turtle()
sam.shape("turtle")
sam.pencolor("#81A1C1")
for i in range(15):
    sam.forward(10)
    sam.penup()
    sam.forward(10)
    sam.pendown()

screen=Screen()
screen.exitonclick()