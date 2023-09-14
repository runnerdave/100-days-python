import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# INSTRUCTIONS
# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

# 3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. 
# On the next level, the car speed increases.

# 4. When the turtle collides with a car, it's game over and everything stops.



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
