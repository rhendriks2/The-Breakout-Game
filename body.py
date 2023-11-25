from turtle import Turtle

RIGHT = 0
LEFT = 180


class Raft(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=9)
        self.goto(position)

    def go_right(self):
        if self.xcor() < 390:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -400:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())


class Block(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(position)

    def remove_block(self):
        self.clear()



