from turtle import Turtle

class Base(Turtle):
    def __init__(self,position) :
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1, 1)
        self.penup()
        self.goto(position)
    def W(self):
        if self.ycor()<255:
            new_y=self.ycor()+20
            self.goto(self.xcor(),new_y)

    def S(self):
        if self.ycor()>-255:
            new_y=self.ycor()-20
            self.goto(self.xcor(),new_y)

    def up(self):
        if self.ycor()<255:
            new_y= self.ycor()+20
            self.goto( self.xcor(),new_y)

    def down(self):
        if self.ycor()>-255:
            new_y= self.ycor()-20
            self.goto(self.xcor(),new_y)