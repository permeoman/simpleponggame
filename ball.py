from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_move = 0
        self.y_move = 10
        random_x = random.randint(-120, 120)
        self.goto(x=random_x, y=300)

    def move_ball(self):
        new_y = self.ycor() - self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)

    def bounce_ball_on_paddle(self):
    #RANDOM RANGE FOR X WILL BOUNCW THW BALL IN EITHER DIRECTION
        self.x_move = random.randint(-10, 10)
    #-1 * 10 WILL GIVE -10 THE THE NEW_Y = CURRENT Y COR - (-10),
    # WHICH BECOMES + AND HENCE RESULTS IN INCREASE IN Y COR OF THE BALL
        self.y_move *= -1

    def bounce_ball_on_up_wall(self):
    #same reason for random
        self.x_move = random.randint(-10, 10)
    # multiplied bt -1 because after bouncing off the paddle the new_y = current_y + Y_move
    # But multiplying -1 causes the + to - so ycor decreases
        self.y_move *= -1

    def bounce_ball_on_side_wall(self):
        if self.xcor in range(-1, 0):
            self.x_move *= 1
        else:
            self.x_move *= -1






