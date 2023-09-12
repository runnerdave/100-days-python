from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 48, "normal")

class Scoreboard(Turtle):

    def __init__(self, height, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.up()
        self.goto(0, height//2 - height//8)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score1}            {self.score2}", align=ALIGN, font=FONT)