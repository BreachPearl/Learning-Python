from turtle import Turtle
from turtle import Screen
from base import Base
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
score=Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
sam=Turtle()
sam.penup()
sam.goto(0,300)
sam.setheading(270)
sam.color("white")
sam.pensize(5)

for y in range (0,20):
    sam.pendown()
    sam.forward(10)
    sam.penup()
    sam.forward(20)

left_base=Base((-387,0))
right_base=Base((380,0))
ball1=Ball()

screen.listen()
screen.onkey(right_base.up, "Up")
screen.onkey(right_base.down, "Down")
screen.onkey(left_base.W, "w")
screen.onkey(left_base.S, "s")
game_is_on=True

while game_is_on:
    time.sleep(ball1.move_speed)
    screen.update()
    ball1.move()
    #detect collision of ball with the upper wall
    if ball1.ycor()>280 or ball1.ycor()<-275:
        ball1.bounce_y()
    #detect the collsion of ball with the base
    if ball1.distance(right_base)<50 and ball1.xcor()>355 or ball1.distance(left_base)<50 and ball1.xcor()<-360:
        ball1.bounce_x()
    #detect right base misses
    if ball1.xcor()>380:
        ball1.reset_position()  
        score.l_point()
    #detect left base misses
    if ball1.xcor()<-385:
        ball1.reset_position()
        score.r_point()
screen.mainloop()
