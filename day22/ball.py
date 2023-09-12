from turtle import Turtle


SW = 225
SE = 315
STEP = 50

class Ball(Turtle):
    def __init__(self, left: bool = True, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.speed("slow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.setheading(SW) if left else self.setheading(SE)
        self.color("white")
        self.move()

    def move(self):
        self.forward(STEP)

