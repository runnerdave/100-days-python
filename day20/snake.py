from turtle import Turtle

STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def create_snake(self):
        x = 0
        for _ in range(3):
            t = Turtle("square")
            t.up()
            t.color("white")
            t.goto(x, 0)
            x -= STEP
            self.snake.append(t)

    def move(self):
        snake = self.snake
        for i in range(len(snake) - 1, 0, -1):
            new_x = snake[i-1].xcor()
            new_y = snake[i-1].ycor()
            snake[i].goto(new_x, new_y)
        self.head.forward(STEP)

    def grow(self):
        t = Turtle("square")
        t.up()
        t.color("white")
        t.goto(self.tail.xcor()-STEP, self.tail.ycor()-STEP)
        self.snake.append(t)
        self.tail = self.snake[-1]

    def crash_with_self(self) -> bool:
        for p in range(1, len(self.snake)):
            if self.snake[p].distance(self.head) == 0:
                return True
        return False


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
