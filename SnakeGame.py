import turtle
from Food import Food
import time
from MakeSnakeMovSnake import Snake
from score import *

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.rt, "Right")
screen.onkey(snake.lt, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
food = Food()
score_board = ScoreBoard()
game = True
while game:
    snake.move()
    screen.update()
    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        score_board.update()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score_board.gameover()
        game = False
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            score_board.gameover()
            game = False
screen.exitonclick()
