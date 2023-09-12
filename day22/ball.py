from turtle import Turtle
import math

STEP = 50


class Ball(Turtle):
    def __init__(self, width, height, right: bool = True, shape: str = "circle", visible: bool = True) -> None:
        super().__init__(shape, visible)
        hyp = math.sqrt((width//2)**2 + (height//2)**2)
        self.angle = math.degrees(math.asin((height//2) / hyp))
        self.limit_x = width//2
        self.limit_y = height//2
        self.penup()
        self.speed("slow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.setheading(self.angle) if right else self.setheading(
            self.angle+180)
        self.color("white")
        self.move()

    def move(self) -> int:
        if self.xcor() > (self.limit_x - STEP):
            return 1
        if self.xcor() < -self.limit_x - STEP:
            return -1
        self.forward(STEP)
        return 0

    def bounce(self):
        self.setheading(self.angle + 90)
        self.forward(STEP)
