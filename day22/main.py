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
RIGHT_PADEL_POS = (WIDTH//2-50, 0)
LEFT_PADEL_POS = (-WIDTH//2+50, 0)


def detect_wall_collision(HEIGHT, ball):
    if ball.ycor() > (HEIGHT//2 - 20) or ball.ycor() < -(HEIGHT//2 - 20):
        ball.bounce_y()


def detect_right_padel_collision(paddle_right, ball):
    if paddle_right.distance(ball) < 50 and ball.xcor() > (RIGHT_PADEL_POS[0] - 10):
        ball.bounce_x()

def detect_left_padel_collision(paddle_left, ball):
    if paddle_left.distance(ball) < 50 and ball.xcor() < (LEFT_PADEL_POS[0] + 10):
        ball.bounce_x()


if __name__ == '__main__':
    screen = Screen()
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    net = Net(HEIGHT)
    scoreboard = Scoreboard(HEIGHT)
    paddle_right = Paddle(screen_h=HEIGHT, pos=RIGHT_PADEL_POS)
    paddle_left = Paddle(pos=LEFT_PADEL_POS)
    ball = Ball(right=True, height=HEIGHT, width=WIDTH)
    screen.update()

    screen.listen()
    screen.onkey(fun=paddle_right.up, key="Up")
    screen.onkey(fun=paddle_right.down, key="Down")
    screen.onkey(fun=paddle_left.up, key="q")
    screen.onkey(fun=paddle_left.down, key="a")

    end = 0
    while end == 0:
        time.sleep(0.1)
        screen.update()
        end = ball.move()
        detect_right_padel_collision(paddle_right, ball)
        detect_left_padel_collision(paddle_left, ball)
        detect_wall_collision(HEIGHT, ball)

    if end == 1:
        scoreboard.score1 += 1
    else:
        scoreboard.score2 += 1
    scoreboard.update_score()

    screen.exitonclick()
