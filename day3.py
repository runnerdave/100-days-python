#!/usr/bin/env python3

# teacher solution: https://replit.com/@appbrewery/treasure-island-end?v=1
# tutorial on transforming image to ascii art https://levelup.gitconnected.com/python-ascii-art-generator-60ba9eb559d7

import PIL.Image


def print_treasure():
    path = 'treasure_chest_transparent.png'

    # load image
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")

    # resize image and turn to grayscale
    image = to_greyscale(resize(image, 50))

    ascii_str = pixel_to_ascii(image)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    print(ascii_img)


def resize(image, new_width=100):
    width, height = image.size
    new_height = new_width * height // width
    return image.resize((new_width, new_height))


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


text_dictionary = {
    "introduction": """
                    Welcome to Treasure Island.
                    Your mission is to find the treasure.
                    You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n""",
    "first_over": "You fell into a hole. Game Over.",
    "left": """You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n""",
    "second_over": "You get attacked by an angry trout. Game Over.",
    "wait": "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n",
    "red_over": "It's a room full of fire. Game Over.",
    "blue_over": "You enter a room of beasts. Game Over.",
    "colour_over": "You chose a door that doesn't exist. Game Over.",
    "win": "You found the treasure! You Win!"
}


def game():
    first_step = input(f'{text_dictionary["introduction"]}')
    if first_step != "left":
        print(text_dictionary["first_over"])
        return
    second_step = input(f'{text_dictionary["left"]}')
    if second_step != "swim":
        print(text_dictionary["second_over"])
        return
    third_step = input(f'{text_dictionary["wait"]}')
    match third_step:
        case "yellow":
            print(text_dictionary["win"])
        case "red":
            print(text_dictionary["red_over"])
        case "blue":
            print(text_dictionary["blue_over"])
        case _:
            print(text_dictionary["colour_over"])


if __name__ == '__main__':
    print_treasure()
    game()
