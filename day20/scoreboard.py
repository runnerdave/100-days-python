from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.update_score()
        

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def finish(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()