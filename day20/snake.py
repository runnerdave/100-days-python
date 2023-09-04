from turtle import Turtle

STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_LENGTH = 10


class Snake:

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def create_snake(self):
        x = 0
        for _ in range(INITIAL_LENGTH):
            pos = (x, 0)
            t = self.create_segment(pos)
            x -= STEP
            self.snake.append(t)

    def create_segment(self, pos):
        t = Turtle("square")
        t.up()
        t.color("white")
        t.goto(pos)
        return t

    def move(self):
        snake = self.snake
        for i in range(len(snake) - 1, 0, -1):
            new_x = snake[i-1].xcor()
            new_y = snake[i-1].ycor()
            snake[i].goto(new_x, new_y)
        self.head.forward(STEP)

    def grow(self):
        t = self.create_segment(self.tail.pos())
        self.snake.append(t)
        self.tail = self.snake[-1]

    def crash_with_self(self) -> bool:
        for p in self.snake[1:]:
            if p.distance(self.head) < 10:
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
