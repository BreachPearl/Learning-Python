from turtle import Turtle, Screen
import random

def rhcolor():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
sam=Turtle()
screen=Screen()
sam.speed("fastest")

for i in range(0,400,5):
    sam.setheading(i)
    sam.pencolor(rhcolor())
    sam.circle(150)

screen.mainloop()