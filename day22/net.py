from turtle import Turtle

SEGMENT_LENGTH = 3
SPACE_LENGTH = 2
COLOR = "white"
SHAPE = "square"

class Net(Turtle):

    def __init__(self, height) -> None:
        self.height = height
        self.create_net()

    def create_segment(self, pos):
        t = Turtle(SHAPE)
        t.up()
        t.color(COLOR)
        t.goto(pos)
        return t
    
    def create_net(self):
        y = self.height/2
        for _ in range(self.height//2, -self.height//2, SPACE_LENGTH):
            pos = (0, y)
            t = self.create_segment(pos)
            y += SEGMENT_LENGTH
            self.snake.append(t)