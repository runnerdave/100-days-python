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
MAX_SCORE = 10

def detect_wall_bounce(HEIGHT, ball):
    if ball.ycor() > (HEIGHT//2 - 20) or ball.ycor() < -(HEIGHT//2 - 20):
        ball.bounce_y()


def detect_right_padel_bounce(paddle_right, ball):
    if paddle_right.distance(ball) < 50 and ball.xcor() > (RIGHT_PADEL_POS[0] - 10):
        ball.bounce_x()

def detect_left_padel_bounce(paddle_left, ball):
    if paddle_left.distance(ball) < 50 and ball.xcor() < (LEFT_PADEL_POS[0] + 10):
        ball.bounce_x()


def handle_score(scoreboard, ball, side):
    if side == 0:
        return 0
    elif side == 1:
        scoreboard.score1 += 1        
    else:
        scoreboard.score2 += 1
    scoreboard.update_score()
    ball.reset_position()
    if scoreboard.score1 == MAX_SCORE or scoreboard.score2 == MAX_SCORE:
        scoreboard.finish_game()
        return MAX_SCORE
    return 0

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
    ball = Ball(height=HEIGHT, width=WIDTH)
    screen.update()

    screen.listen()
    screen.onkey(fun=paddle_right.up, key="Up")
    screen.onkey(fun=paddle_right.down, key="Down")
    screen.onkey(fun=paddle_left.up, key="q")
    screen.onkey(fun=paddle_left.down, key="a")

    end = 0
    while end == 0:
        time.sleep(ball.move_speed)
        screen.update()
        end = ball.move()
        detect_right_padel_bounce(paddle_right, ball)
        detect_left_padel_bounce(paddle_left, ball)
        detect_wall_bounce(HEIGHT, ball)
        end = handle_score(scoreboard, ball, end)

    screen.exitonclick()
