from turtle import Turtle

LEFT = 180
RIGHT = 0
MOVE = 25


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1.6)
        self.color("white")
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        self.setheading(LEFT)
        self.forward(MOVE)

    def move_right(self):
        self.setheading(RIGHT)
        self.forward(MOVE)
