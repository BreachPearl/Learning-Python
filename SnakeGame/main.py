from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

sn = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
screen.onkey(sn.left, "Left")
screen.onkey(sn.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    sn.move()

    #Detect collision with food.
    if sn.head.distance(food) < 15:
        food.refresh()
        sn.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in sn.segments:
        if segment == sn.head:
            pass
        elif sn.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()