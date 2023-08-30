# solution from teacher: https://replit.com/@appbrewery/hirstpainting-final

import colorgram
import turtle as t

import os
import random

absolute_path = os.path.dirname(__file__)
relative_path = ""
full_path = os.path.join(absolute_path, relative_path)

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")


def extract_colors_from_image(image, colors=30):
    colors = colorgram.extract(full_path + image, colors)
    return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]


def draw_matrix(palette, width=10, height=10, space=50):
    for _ in range(width):
        for _ in range(height):
            colour = random.choice(palette)
            draw_dot(colour)
            tim.penup()
            tim.forward(space)
        tim.backward(10*height + 8 * space)
        tim.left(90)
        tim.forward(50)
        tim.right(90)

def set_start():
    tim.up()
    tim.backward(200)
    tim.right(90)
    tim.forward(200)
    tim.left(90)

def draw_dot(colour):
    tim.begin_fill()
    tim.color(colour)
    tim.circle(10)
    tim.end_fill()


if __name__ == '__main__':
    colors = extract_colors_from_image('graphic.jpeg')
    set_start()
    draw_matrix(colors)
    screen = t.Screen()
    screen.exitonclick()
