from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.high_score = self.read_data()
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}     High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_score(self):
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        if self.high_score < self.score:
            self.high_score = self.score
            self.save_high_score(str(self.high_score))
        self.update_score()

    def read_data(self) -> int:
        with open("./data.txt") as data:
            return int(data.read())

    def save_high_score(self, high_score):
        with open("data.txt", "w") as data:
            data.write(high_score)
