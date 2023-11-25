from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#29ADB2")
        self.goto(x=0, y=-210)
        self.x_move = 13
        self.y_move = 13
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(x=0, y=-230)
        self.move_speed = 0.1
        self.bounce_y()
