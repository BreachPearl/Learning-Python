from turtle import Turtle, Screen
import random
sam=Turtle()
screen=Screen()
sam.shape("turtle")
angles=[60,90,108,120,128.57,135,140,144 ]
sides=[3,4,5,6,7,8,9,10]
colors=['#a3e1f7', '#8b9ac4', '#2f4a93', '#d2e5b7', '#9d2c3e', '#5f3e91', '#bbfa4c', '#7a91bc', '#ab6d89', '#fdc04d']

for index, angle in enumerate(angles):
    sam.pencolor(random.choice(colors))
    for _ in range(sides[index]):
        sam.forward(100)
        sam.right(180 - angle)
screen.mainloop()


# another way to write this code

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)