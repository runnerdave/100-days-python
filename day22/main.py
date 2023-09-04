from turtle import Screen, Turtle
from net import Net

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

WIDTH = 600
HEIGHT = 600

if __name__ == '__main__':
    screen = Screen()
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor("black")
    screen.title("Pong")
    # screen.tracer(0)

    net = Net(HEIGHT)


    screen.exitonclick()