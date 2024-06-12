from turtle import Turtle, Screen
import random

def rhcolor():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
sam=Turtle()
screen=Screen()
sam.pensize(10)
direc=[sam.left,sam.right]
move=[sam.forward,sam.backward]
for _ in range(0,50):
    sam.pencolor(rhcolor())
    random.choice(direc)(90)
    random.choice(move)(50)
    
screen.mainloop()