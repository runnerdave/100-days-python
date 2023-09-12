from turtle import Turtle

UP = 90
DOWN = 270
WIDTH = 1
HEIGHT = 5
STEP = 20
COLOR = "white"
SHAPE = "square"

class Paddle(Turtle):
    def __init__(self, width=WIDTH, height=HEIGHT, pos=(350, 0), shape="square", screen_h=600) -> None:
        super().__init__(shape)
        self.turtlesize(stretch_wid=width, stretch_len=height)
        self.color(COLOR)
        self.penup()
        self.setheading(90)
        self.goto(pos)
        self.screen_max_y = screen_h//4 + HEIGHT*STEP
    
    def up(self):
        if self.ycor() < self.screen_max_y:
            self.forward(HEIGHT*STEP/2)

    def down(self):
        if self.ycor() > -self.screen_max_y:
            self.backward(HEIGHT*STEP/2)



