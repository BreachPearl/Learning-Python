import colorgram
from turtle import Turtle, Screen
import random

sam=Turtle()
screen=Screen()
screen.colormode(255)
sam.speed("fastest")
sam.penup()
sam.hideturtle()

# rgb_colrs=[]
# colors=colorgram.extract('C:\Learning Python\TurtleArt\hirst.jpg',10)              #here we used 
# for color in colors:                                                               #this code to extract the colors from the image   
#     r=color.rgb.r                                                                  #and get the rgb codes
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colrs.append(new_color)
final_colors=[(250, 246, 241), (250, 244, 247), (241, 249, 245), (242, 245, 249), (207, 155, 102), (58, 107, 128), (162, 82, 44), (123, 156, 171), (125, 80, 98), (126, 175, 159)]
sam.setheading(225)
sam.forward(300)
sam.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    sam.dot(20, random.choice(final_colors))
    sam.forward(50)

    if dot_count % 10 == 0:
        sam.setheading(90)
        sam.forward(50)
        sam.setheading(180)
        sam.forward(500)
        sam.setheading(0)

screen.mainloop()