from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_STARTING_POSITIONS = [i for i in range(-230, 250, 45)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, number_of_cars=10) -> None:
        self.cars = []
        self.number_of_cars = number_of_cars
        self.move_speed = 0.4

    def generate_traffic(self):
        for _ in range(self.number_of_cars):
            car = self.make_car()
            self.cars.append(car)

    def move(self):
        for c in self.cars:
            c.forward(MOVE_INCREMENT)
            if c.xcor() < -260:
                c.goto(300, c.ycor())


    def make_car(self):
        color = random.choice(COLORS)
        rand_x = random.randint(-300, 300)
        rand_y = random.choice(Y_STARTING_POSITIONS)
        position = (rand_x, rand_y)
        car = Turtle()
        car.color(color)
        car.penup()
        car.turtlesize(stretch_wid=2, stretch_len=4)
        car.goto(position)
        car.shape("square")
        car.setheading(180)
        return car
        
