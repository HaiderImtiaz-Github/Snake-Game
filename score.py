
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        super().penup()
        super().hideturtle()
        self.score = 0
        super().color("white")
        super().pensize(3)
        super().goto(-50, 260)
        super().write(f"Score : {self.score}", font=("Arial", 24, "normal"))

    def update(self):
        self.score += 1
        super().clear()
        super().write(f"Score : {self.score}", font=("Arial", 24, "normal"))

    def gameover(self):
        super().goto(-60, 0)
        super().write("Game Over", font=("Arial", 24, "normal"))
