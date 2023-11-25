import time
import turtle as t
from body import Raft, Block
from ball import Ball
from scoreboard import Scoreboard, Lives

screen = t.Screen()
screen.setup(width=1000, height=500)
screen.title("The Breakout Game")
screen.bgcolor("black")
screen.tracer(0)


raft = Raft((0, -230))
ball = Ball()
scoreboard = Scoreboard()
number_of_lives = Lives()

screen.listen()
screen.onkey(fun=raft.go_right, key="Right")
screen.onkey(fun=raft.go_left, key="Left")
screen.onkey(fun=raft.go_right, key="a")
screen.onkey(fun=raft.go_right, key="d")


def play_game():
    global game_is_on
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with the raft and upper wall
    if ball.distance(raft) < 90 and ball.ycor() < -215 or ball.ycor() > 230:
        ball.bounce_y()
        # can add increase speed functionality when ball collides with the raft

    # collision with side walls
    if ball.xcor() <= -480 or ball.xcor() >= 480:
        ball.bounce_x()

    # creating the blocks
    x_cor = [-480]
    x = -480
    for n in range(1000):
        if x <= 469:
            x_value = x + 25
            x_cor.append(x_value)
            x = x_value

    y_cor = [150, 126, 102, 78]
    block_colors = ["#7743DB", "#F4CE14", "#64CCC5", "#CD5C08"]
    blocks_list = []

    c_ps = 0
    for y in y_cor:
        color = block_colors[c_ps]
        for x in x_cor:
            block_position = (x, y)
            block = Block(color, block_position)
            blocks_list.append(block)
        c_ps += 1

    # detect collision with block
    for block in blocks_list:
        if ball.distance(block) < 22:
            ball.bounce_y()
            block.remove_block()
            scoreboard.score += 4
            scoreboard.update_scoreboard()

    # check for game over
    if ball.ycor() < -240:
        ball.reset_position()
        number_of_lives.lives -= 1
        if number_of_lives.lives < 0:
            game_is_on = False
            if scoreboard.score > int(scoreboard.high_score):
                with open("data.txt", mode="w") as data:
                    data.write(str(scoreboard.score))
            scoreboard.game_over(screen)

        else:
            number_of_lives.update_lives()


game_is_on = True
while game_is_on:
    play_game()


screen.exitonclick()
