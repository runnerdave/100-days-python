from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape="turtle") -> None:
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.color("red")
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(10)
    
    def reset(self):
        self.goto(STARTING_POSITION)
        