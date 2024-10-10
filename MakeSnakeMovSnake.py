import turtle
from turtle import *
import time

POSN = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
TIME_DELAY = 0.1
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):

        self.segment = []
        self.creat_snake()
        self.head = self.segment[0]

    def creat_snake(self):
        for posn in POSN:
            self.add_seg(posn)

    def add_seg(self, posn):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(posn)
        self.segment.append(new_segment)

    def extend(self):
        self.add_seg(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)
        time.sleep(TIME_DELAY)

    def rt(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def lt(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
