from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd
import os
import random
current_directory = os.path.dirname(os.path.abspath(__file__))
images_directory = "images"
data_directory = "data"

BACKGROUND_COLOR = "#B1DDC6"

def prep_image(path, size):
    og = Image.open(path)
    resized = og.resize(size)
    img = ImageTk.PhotoImage(resized)
    return img

def change_word():
    new_word = random.choice(german_dict)
    canvas.itemconfig(title_text, text=list(new_word.keys())[False])
    canvas.itemconfig(word_text, text=new_word['german'])


french_words = pd.read_csv(os.path.join(current_directory, data_directory, 'french_words.csv'))
french_dict = french_words.to_dict('records')

german_words = pd.read_csv(os.path.join(current_directory, data_directory, 'german-top-words.csv'))
german_dict = german_words.iloc[:, 1:].to_dict('records')

card_back = "card_back.png"
card_back_path = os.path.join(current_directory, images_directory, card_back)

card_front = "card_front.png"
card_front_path = os.path.join(current_directory, images_directory, card_front)

right = "right.png"
right_path = os.path.join(current_directory, images_directory, right)

wrong = "wrong.png"
wrong_path = os.path.join(current_directory, images_directory, wrong)

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=400, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

card_back_img = prep_image(card_back_path, (350, 300))
card_front_img = prep_image(card_front_path, (400, 300))

canvas.create_image(200, 200, image=card_front_img)
title_text = canvas.create_text(200, 150, fill="black", text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(200, 220, fill="black", text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = prep_image(right_path, (50,50))
right_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=change_word)
right_button.grid(column=0, row=1)

wrong_img = prep_image(wrong_path, (50,50))
wrong_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=change_word)
wrong_button.grid(column=1, row=1)

window.mainloop()
