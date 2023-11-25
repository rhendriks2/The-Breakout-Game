from turtle import Turtle

FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=270, y=230)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", font=FONT)

    def game_over(self, screen):
        screen.clear()
        screen.bgcolor("black")
        self.clear()
        self.goto(x=-150, y=0)
        self.write(f"GAME OVER!\n     Score: {self.score}", font=("Arial", 30, "bold"))


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=-400, y=230)
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.write(f"Lives: {self.lives}", font=FONT)


