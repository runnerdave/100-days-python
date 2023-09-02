from turtle import Screen
import time
from scoreboard import Scoreboard
from food import Food

from snake import Snake

WIDTH = 600
HEIGHT = 600


def check_food_collision(snake, food, scoreboard):
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.increase_score()
        snake.grow()


def finish(scoreboard):
    scoreboard.finish()


def crash_with_edges(snake) -> bool:
    if snake.head.xcor() > (WIDTH / 2) or snake.head.xcor() < -(WIDTH / 2):
        scoreboard.finish()
        return True
    if snake.head.ycor() > (HEIGHT / 2) or snake.head.ycor() < -(HEIGHT / 2):
        scoreboard.finish()
        return True
    return False


if __name__ == '__main__':
    screen = Screen()
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor("black")
    screen.title("My snake game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while not crash_with_edges(snake) and not snake.crash_with_self():
        time.sleep(0.4)
        screen.update()
        snake.move()
        check_food_collision(snake, food, scoreboard)

    screen.exitonclick()
