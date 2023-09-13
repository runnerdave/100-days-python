from turtle import Turtle
import math

STEP = 10


class Ball(Turtle):
    def __init__(self, width, height, shape: str = "circle", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.limit_x = width//2
        self.limit_y = height//2
        self.penup()
        self.speed("slow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.move_x = STEP
        self.move_y = STEP
        self.move_speed = 0.1
        self.move()

    def move(self) -> int:
        # Detect if pass paddle x position to score
        if self.xcor() > (self.limit_x - STEP):
            return 1
        if self.xcor() < -self.limit_x - STEP:
            return -1
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
        return 0

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_speed *= 0.5        
        self.move_x *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.move_x *= -1
        self.goto((0, 0))
        
