from turtle import Turtle, Screen
import random
sam=Turtle()
screen=Screen()
def akey():
    sam.lt(10)
def dkey():
    sam.right(10)
def wkey():
    sam.forward(10)
def skey():
    sam.backward(10)
def ckey():
    sam.clear()
screen.onkey(wkey, "w")
screen.onkey(skey, "s")
screen.onkey(dkey, "d")
screen.onkey(akey, "a")
screen.onkey(ckey, "c")
screen.listen()


screen.mainloop()