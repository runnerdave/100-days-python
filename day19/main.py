from turtle import Turtle, Screen
import random

colors = ["blue", "yellow", "green", "purple", "red", "orange"]


class Bale:
    def __init__(self) -> None:
        self.turtles = []
        self.__build()

    def hatch(self):
        for c in colors:
            self.turtles.append(NinjaTurtle(c))

    def place_at_start(self, x=-230, y=180):
        for t in self.turtles:
            t.tim.goto(x, y)
            y -= 50

    def race(self):
        finish_line = 200
        winner = None
        while winner == None:
            for t in self.turtles:
                x = t.tim.xcor()
                y = t.tim.ycor()
                factor = random.randint(5, 10)
                if x + factor >= finish_line:
                    winner = t
                t.tim.goto(x + factor, y)
        return winner.tim.pencolor()

    def __build(self):
        self.hatch()
        self.place_at_start()


class RaceCourse:
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(height=500, width=500)
        self.user_bet = self.screen.textinput(
            title="Place your bet", prompt="Which turtle you think will win? Choose a colour")

    def exit(self):
        self.screen.exitonclick()


class NinjaTurtle:
    def __init__(self, color):
        self.tim = Turtle(shape="turtle")
        self.tim.color(color)
        self.tim.up()


if __name__ == '__main__':
    raceCourse = RaceCourse()
    bale = Bale()
    winner = bale.race()
    print(f"The winner is: {winner}")
    print(f"You {'win' if winner == raceCourse.user_bet else 'lose'}!")
    raceCourse.exit()
