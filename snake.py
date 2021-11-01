from turtle import Turtle,Screen
import time


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtle_obj_list = []
        self.i = 0
        self.create_snake()
        self.head = self.turtle_obj_list[0]

    def create_snake(self):
        for _ in range(3):
            turtle_obj = Turtle(shape="square")
            turtle_obj.penup()
            turtle_obj.color("white")
            turtle_obj.setx(self.i)
            self.i = self.i - 20
            self.turtle_obj_list.append(turtle_obj)

    def move(self):
        for index in range(len(self.turtle_obj_list) - 1, 0, -1):
            new_x = self.turtle_obj_list[index - 1].xcor()
            new_y = self.turtle_obj_list[index - 1].ycor()
            self.turtle_obj_list[index].goto(new_x, new_y)
        self.turtle_obj_list[0].forward(20)

    def increase_snake(self):
        turtle_obj = Turtle(shape="square")
        turtle_obj.penup()
        turtle_obj.color("white")
        turtle_obj.goto(self.turtle_obj_list[-1].xcor(),self.turtle_obj_list[-1].ycor())
        self.turtle_obj_list.append(turtle_obj)

    def check_tail_collision(self):
        for segment in self.turtle_obj_list[1:]:
            if self.head.distance(segment) < 10:
                return True

    def up(self):
        if self.turtle_obj_list[0].heading() != DOWN:
            self.turtle_obj_list[0].setheading(90)
    def left(self):
        if self.turtle_obj_list[0].heading() != RIGHT:
            self.turtle_obj_list[0].setheading(180)
    def right(self):
        if self.turtle_obj_list[0].heading() != LEFT:
            self.turtle_obj_list[0].setheading(0)
    def down(self):
        if self.turtle_obj_list[0].heading() != UP:
            self.turtle_obj_list[0].setheading(270)


