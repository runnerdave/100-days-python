import time
from turtle import Screen
from ball import Ball
from net import Net
from paddle import Paddle
from scoreboard import Scoreboard

# PONG!
# Classes:
# - Paddle
#   - Length, move_up, move_down, 
# - Ball
#   - launch, bounce, move, touch wall
# - Scoreboard
#   - score_counter, call game_over, score
# - Net
#   - Length, Segment_length, Segment_space, draw_itself

WIDTH = 800
HEIGHT = 600

if __name__ == '__main__':
    screen = Screen()
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    is_game_on = True
    net = Net(HEIGHT)
    scoreboard = Scoreboard(HEIGHT)
    paddle_right = Paddle(screen_h=HEIGHT)
    paddle_left = Paddle(pos=(-350, 0))
    ball = Ball(True)
    screen.update()

    screen.listen()
    screen.onkey(fun=paddle_right.up, key="Up")
    screen.onkey(fun=paddle_right.down, key="Down")
    screen.onkey(paddle_left.up, "q")
    screen.onkey(paddle_left.down, "a")

    i = 0
    while is_game_on and not i == 200:
        time.sleep(0.4)
        screen.update()
        ball.move()
        i += 1

    screen.exitonclick()