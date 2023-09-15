import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

# INSTRUCTIONS
# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

# 3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. 
# On the next level, the car speed increases.

# 4. When the turtle collides with a car, it's game over and everything stops.


def score(player: Player, scoreboard: Scoreboard, cars: CarManager):
    if player.ycor() == FINISH_LINE_Y:
        cars.move_speed *= 0.5
        scoreboard.score += 1
        scoreboard.update_score()

def detect_crash(player: Player, cars) -> bool:
    for c in cars:
        if player.distance(c) <= 20:
            return True     
    return False

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle crossing")
    screen.tracer(0)

    player = Player()
    scoreboard = Scoreboard()
    cars = CarManager()
    cars.generate_traffic()

    screen.listen()
    screen.onkey(fun=player.up, key="Up")
    
    game_is_on = True
    while game_is_on:
        time.sleep(cars.move_speed)
        score(player, scoreboard, cars)
        cars.move()
        if detect_crash(player, cars.cars):
            scoreboard.game_over()
            game_is_on = False
        screen.update()

    screen.exitonclick()
