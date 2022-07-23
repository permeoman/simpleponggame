from turtle import Turtle

FONTS = ("Courier", 15, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"SCORE:{self.score}", align="center", font=FONTS)

    def update_score(self):
        self.keep_score()
        self.clear()
        self.write(f"SCORE:{self.score} ", align="center", font=FONTS)

    def keep_score(self):
        self.score += 1

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER",  align="center", font=FONTS)


