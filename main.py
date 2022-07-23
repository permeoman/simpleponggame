from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=300, height=600)
screen.title("BOUNCE GAME")
screen.tracer(0)
screen.listen()

paddle = Paddle()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")

ball = Ball()
score = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move_ball()
#DETECTS COLLISION BETWEEN BALL AND PADDLE
    if ball.distance(paddle) < 30:
        ball.bounce_ball_on_paddle()
        score.update_score()
#DETECTS COLLISION WITH UPPER WALL
    if ball.ycor() > 290:
        ball.bounce_ball_on_up_wall()
#DETECTS COLLISION WITH SIDE WALL
    if ball.xcor() > 140 or ball.xcor() < -140:
        ball.bounce_ball_on_side_wall()
#DETECT WHEN GAME OVER
    if ball.ycor() < -290:
        score.game_over()






screen.exitonclick()